#!/usr/bin/env bash

# Exit with nonzero exit code if anything fails (-e)
# Print all executed lines (-x)
set -ex

# Commit sha of master branch
SHA=`git rev-parse --verify HEAD`
TARGET_BRANCH="gh-pages"

if [ "${GITHUB_ACTIONS}" != "true" ]; then
    echo "Skipping deploy; just doing a build."
    exit 0
fi

# Move html to temp dir
mv build ../page-build
git checkout "${TARGET_BRANCH}" || git checkout --orphan "${TARGET_BRANCH}"
rm -rf .github .pre-commit-config.yaml .gitignore * || exit 0
cp -r ../page-build/* .

git config user.name "${COMMIT_AUTHOR}"
git config user.email "${COMMIT_AUTHOR_EMAIL}"

git add -A .
# If there are no changes to the compiled out (e.g. this is a README update) then just bail.
if git diff --cached --quiet; then
    echo "No changes to the output on this push; exiting."
    exit 0
fi

git commit -m "Deploy to GitHub Pages: ${SHA}"
