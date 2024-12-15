# buildozer.spec

[app]
# (str) Title of your application
title = BudgetTracker

# (str) Package name
package.name = budgettracker

# (str) Package domain (e.g. org.myname.myapp)
package.domain = org.example

# (list) Source files to include (comma-separated extensions)
source.include_exts = py,kv

# (list) Application requirements
# In this case, we need Python3 and Kivy
requirements = python3, kivy

# (str) Application version
version = 1.0

# (str) Application release
# You can leave this as default, or set a custom version
# release = 1.0

# (str) Custom source folder (default is current folder)
# source.dir =

# (list) Additional Java .jar files to include in the APK
# java.sources =

# (str) Name of the main .py file (e.g. "main.py")
# main.py is usually the default, but you can change it if needed
source.include_exts = py,kv

# (list) Other directories to include (comma-separated list of paths)
# source.include_dirs =

# (list) Files to include
# source.include_files =

[buildozer]
# (str) Which buildozer version to use (use latest stable by default)
# buildozer.version = 1.2.0

# (bool) Whether to use the package for Android or iOS
android = True

# (bool) Whether to run the application on the emulator
android.emulator = False

# (str) Android NDK version
android.ndk = r21e

# (str) Android API level to target
android.api = 29

# (str) Android SDK version
android.sdk = 29

# (bool) Enable verbose mode
# (use -v to get more logging)
verbose = True
