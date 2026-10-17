[app]
title = Tajik Test
package.name = tajiktest
package.domain = org.tajik.test
source.dir = .
source.include_exts = py
version = 0.1
requirements = python3,kivy==2.3.0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.fork = kivy
p4a.branch = develop
android.build_tools_version = 33.0.1