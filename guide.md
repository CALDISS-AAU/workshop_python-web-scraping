# Guide til brug af workshop template



Opret GitHub repo:

Navn: `workshop_[navn]`



Lav en ny side med hugo:

`hugo new site [workshop navn]`



Tilføj workshop template som remote:

`git remote add origin git@github.com:caldissKjelmann/workshop_template.git`



Fetch og reset:

`git fetch origin master`
`git reset --hard FETCH_HEAD`



Tilføj tema

`git submodule add https://github.com/matcornic/hugo-theme-learn.git themes/hugo-theme-learn`



Opret `gh-pages` branch som deployment branch (`deploy_gh-pages.sh`)

https://gohugo.io/hosting-and-deployment/hosting-on-github/#deployment-of-project-pages-from-your-gh-pages-branch



Tilføj indhold med parser script (`parse_ws-md.py`)



Indsæt billeder i static-mappen



Rediger tabeller fra HTML til markdown

https://jmalarcon.github.io/markdowntables/



Ændr forside (`_index.md`)



Opdater `config.toml`

- Main URL skal svare til GitHub Pages URL

