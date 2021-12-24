1. Write changelog in changelog.txt
2. Update addon.xml - the version and the news tag
3. Push to github wait for CI
   - submit PR _upstream_ and merge it, then push to your _personal_ fork
4. Create a new git tag and push it to your _personal_ fork with secrets for the submit action configured
   - `git tag X.X.X && git push --tags`
