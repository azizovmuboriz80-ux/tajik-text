[app]
title = Tajik AI
package.name = tajikai
package.domain = org.tajik.ai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
p4a.branch = develop
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True