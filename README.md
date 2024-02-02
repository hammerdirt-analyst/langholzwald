# Langholzwald

Une évaluation des observations environnementales provenant de sources publiques (citizen science) en relation avec les  _ecosystem services_ (services écosystémiques?) et la conservation d'espèces ciblées.

## Objectifs

Donner aux parties concernées une vue d'ensemble des données actuellement disponibles à partir de ressources fiables. Offrir aux parties concernées un espace pour élaborer un document d'aide à la décision fondé sur des données empiriques et adapté à leur lieu d'intérêt spécifique. Soutenir le développement de forêts durables conformément à [la Guide pour coordonner la conservation des espèces cibles et celle des milieux naturels](https://www.infospecies.ch/fr/assets/content/documents/Plan_dAction_forets_claires-201112-def.pdf).

## Motivation

Cette forêt est proche de ma maison

## Structure
### Ressources

Les publications de référence et les produits de données associés comme les cartes ou les graphiques.

### Cartography

Le dossier de cartographie contient les fichiers .shp édités issus de swissTLM3D 2.1 et les fichiers générés à partir de ceux-ci.

### Structure du fichier de données

#### In process

Les fichiers "en traitement" sont ceux provenant de sources extérieures. Ils sont actuellement comparés à d'autres sources pour déterminer leur adéquation ou nous extrayons les données dans un certain périmètre de la zone d'étude.

#### End pipe

Le "conduit final" contient des fichiers (ou des connexions) qui sont actuellement utilisés pour les graphiques et les diagrammes. Au fur et à mesure que le projet progresse, le dossier "en traitement" se videra (à mesure que nous passerons en revue toutes les données) et le dossier "conduit final" diminuera. Dans certains cas, il peut être possible d'éliminer le stockage de toutes les données en se connectant directement aux sources de données existantes.

## Installed packages

dependencies:
  - python=3.12
  - jupyterlab
  - jupyter-book
  - pandas
  - pyarrow
  - pdfplumber
  - netcdf4
  - xarray
  - watermark




