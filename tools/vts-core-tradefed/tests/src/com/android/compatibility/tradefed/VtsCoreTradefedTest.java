/*
 * Copyright (C) 2019 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.android.compatibility.tradefed;

import static org.junit.Assert.assertEquals;

import com.android.compatibility.common.tradefed.build.CompatibilityBuildHelper;
import com.android.compatibility.common.tradefed.build.CompatibilityBuildProvider;
import com.android.tradefed.build.IBuildInfo;
import com.android.tradefed.config.OptionSetter;
import com.android.tradefed.util.FileUtil;
import java.io.File;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

/** Tests for vts-tradefed. */
@RunWith(JUnit4.class)
public class VtsCoreTradefedTest {
    private static final String PROPERTY_NAME = "VTS_ROOT";
    private static final String SUITE_FULL_NAME = "Vendor Test Suite";
    private static final String SUITE_NAME = "VTS";
    private static final String SUITE_PLAN = "vts";
    private static final String DYNAMIC_CONFIG_URL = "";

    private String mOriginalProperty = null;

    @Before
    public void setUp() {
        mOriginalProperty = System.getProperty(PROPERTY_NAME);
    }

    @After
    public void tearDown() {
        if (mOriginalProperty != null) {
            System.setProperty(PROPERTY_NAME, mOriginalProperty);
        }
    }

    @Test
    public void testSuiteInfoLoad() throws Exception {
        // Test the values in the manifest can be loaded
        File root = FileUtil.createTempDir("root");
        System.setProperty(PROPERTY_NAME, root.getAbsolutePath());
        File base = new File(root, "android-vts");
        base.mkdirs();
        File tests = new File(base, "testcases");
        tests.mkdirs();
        CompatibilityBuildProvider provider = new CompatibilityBuildProvider();
        OptionSetter setter = new OptionSetter(provider);
        setter.setOptionValue("plan", SUITE_PLAN);
        setter.setOptionValue("dynamic-config-url", DYNAMIC_CONFIG_URL);
        IBuildInfo info = provider.getBuild();
        CompatibilityBuildHelper helper = new CompatibilityBuildHelper(info);
        assertEquals("Incorrect suite full name", SUITE_FULL_NAME, helper.getSuiteFullName());
        assertEquals("Incorrect suite name", SUITE_NAME, helper.getSuiteName());
        FileUtil.recursiveDelete(root);
    }
}
