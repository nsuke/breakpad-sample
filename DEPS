use_relative_paths = True

vars = {
  "root_dir": "src",
  "googlecode_url": "http://%s.googlecode.com/svn",
  "sourceforge_url": "http://svn.code.sf.net/p/%(repo)s/code",
  "chromium_trunk" : "http://src.chromium.org/svn/trunk",
  "chromium_revision": "285412",
  "webkit_trunk": "http://src.chromium.org/blink/trunk",
}

deps = {
  "../chromium_deps":
    File(Var("chromium_trunk") + "/src/DEPS@" + Var("chromium_revision")),

  "build":
    Var("chromium_trunk") + "/src/build@" + Var("chromium_revision"),
  "buildtools":
    From("chromium_deps", "src/buildtools"),
  "tools/gn":
    Var("chromium_trunk") + "/src/tools/gn@" + Var("chromium_revision"),
  "tools/generate_library_loader":
    Var("chromium_trunk") + "/src/tools/generate_library_loader@" + Var("chromium_revision"),
  "tools/clang":
    Var("chromium_trunk") + "/src/tools/clang@" + Var("chromium_revision"),
  "third_party/binutils":
    Var("chromium_trunk") + "/src/third_party/binutils@" + Var("chromium_revision"),
  "third_party/clang_format":
    Var("chromium_trunk") + "/src/third_party/clang_format@" + Var("chromium_revision"),

  "testing":
    Var("chromium_trunk") + "/src/testing@" + Var("chromium_revision"),
  "testing/gmock":
    From("chromium_deps", "src/testing/gmock"),
  "testing/gtest":
    From("chromium_deps", "src/testing/gtest"),

  "breakpad":
    Var("chromium_trunk") + "/src/breakpad@" + Var("chromium_revision"),
  "breakpad/src":
    From("chromium_deps", "src/breakpad/src"),
  "third_party/lss":
    From("chromium_deps", "src/third_party/lss"),
}
hooks = [
  {
    "name": "gn_mac",
    "pattern": ".",
    "action": [ "download_from_google_storage",
                "--no_resume",
                "--platform=darwin",
                "--no_auth",
                "--bucket", "chromium-gn",
                "-s", Var("root_dir") + "/buildtools/mac/gn.sha1",
    ],
  },
  {
    "name": "gn_linux",
    "pattern": ".",
    "action": [ "download_from_google_storage",
                "--no_resume",
                "--platform=linux*",
                "--no_auth",
                "--bucket", "chromium-gn",
                "-s", Var("root_dir") + "/buildtools/linux64/gn.sha1",
    ],
  },
  {
    "name": "clang_format_mac",
    "pattern": "third_party/clang_format/bin/mac/clang-format.sha1",
    "action": [ "download_from_google_storage",
                "--no_resume",
                "--platform=darwin",
                "--no_auth",
                "--bucket", "chromium-clang-format",
                "-s", Var("root_dir") + "/buildtools/mac/clang-format.sha1",
    ],
  },
  {
    "name": "clang_format_linux",
    "pattern": "third_party/clang_format/bin/linux/clang-format.sha1",
    "action": [ "download_from_google_storage",
                "--no_resume",
                "--platform=linux*",
                "--no_auth",
                "--bucket", "chromium-clang-format",
                "-s", Var("root_dir") + "/buildtools/linux64/clang-format.sha1",
    ],
  },
  {
    # Pull clang if on Mac or clang is requested via GYP_DEFINES.
    "pattern": ".",
    "action": ["python", Var("root_dir") + "/tools/clang/scripts/update.py",
               "--if-needed"],
  },
  {
    # Pull binutils for gold.
    "name": "binutils",
    "pattern": ".",
    "action": ["python", Var("root_dir") + "/third_party/binutils/download.py"],
  },
  {
    "name": "patch",
    "pattern": ".",
    "action": ["python", Var("root_dir") + "/patches/patch.py", "-I"],
  },
]
