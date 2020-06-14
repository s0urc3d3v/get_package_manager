#GET package manager
## a *nix package manager

#WARNING
Right now everything is over HTTP NOT https.  This might change in the future.
-----

###To add support for a new package by branching
1. add the package name (argument name) to 'packages'
2. add the url to the 'packageURL' at the same index level
3. add the same package name to the correct connection

* This means if the package url is prefixed with http:// or https:// then put the package name in HTTPindex, etc

--------------
##Notes

* May need root to compile software correctly

-----------------
