# Example
Simple exemple de documentation. Pour vérifier que la documentation de la suite de test est bien prise en compte.

## LOG_VARIABLES
Simple affichage des variables pour s'assurer qu'on utilise les bonnes valeurs pour le déroulement des tests.

## GET_INVALID_ROUTE
Tests de requêtes GET sur des routes invalides.

## POST_INVALID_ROUTE
Tests de requêtes POST sur des routes invalides.

## DELETE_INVALID_ROUTE
Tests de requêtes DELETE sur des routes invalides.

## POST_EMPTY_PAYLOAD_EVERY_POST_ROUTE
Tests de requêtes POST avec des payloads vides.

## GET_STATUS
Test de récupération des différentes versions firmwares et du statut de l'appareil.

## CHECK_VERSION
Test de comparaison des différentes versions firmwares à celles attendues. Les versions sont comparées à celle contenues dans le fichier version.txt de l'artefact.

## GET_SWAGGER
Test de la route permettant de récupérer le swagger.

## POST_CONFIGURATION_NETWORK
Test de l'envoi d'une configuration réseau.

## GET_CONFIGURATION_NETWORK
Test de la récupération de la configuration réseau.

## CHECK_CONFIGURATION_NETWORK
Test de comparaison de la configuration réseau à celle attendue. La configuration est comparée à celle envoyée précédemment.

## DELETE_CONFIGURATION_NETWORK
Test de la suppression de la configuration réseau.

## GET_CONFIGURATION_NETWORK_2
Test de la récupération de la configuration réseau après suppression de celle-ci.

## DELETE_CONFIGURATION_NETWORK_2
Test de la suppression de la configuration réseau avec aucune configuration présente.

## CHECK_CONFIGURATION_NETWORK_2
Test de comparaison de la configuration réseau à celle attendue. La configuration est comparée à celle envoyée précédemment.

## POST_CONFIGURATION_MQTT
Test de l'envoi d'une configuration mqtt.

## GET_CONFIGURATION_MQTT
Test de la récupération de la configuration mqtt.

## DELETE_CONFIGURATION_MQTT
Test de suppression de la configuration mqtt.

## GET_CONFIGURATION_MQTT_2
Test de la récupération de la configuration mqtt après suppression de celle-ci.

## DELETE_CONFIGURATION_MQTT_2
Test de la suppression de la configuration mqtt avec aucune configuration présente.

## POST_METRICS_BROKER_0
Test de l'envoi d'une configuration d'envoi de valeurs des capteurs en mqtt.

## GET_METRICS_BROKER_0
Test de la récupération de la configuration d'envoi de valeurs des capteurs en mqtt.

## DELETE_METRICS_BROKER_0
Test de la suppression de la configuration d'envoi de valeurs des capteurs en mqtt.

## GET_METRICS_BROKER_0_2
Test de la récupération de la configuration d'envoi de valeurs des capteurs en mqtt après suppression de celle-ci.

## DELETE_METRICS_BROKER_0_2
Test de la suppression de la configuration d'envoi de valeurs des capteurs en mqtt avec aucune configuration présente.

## POST_CA_CERT
Test de l'envoi du certificat CA.

## DELETE_CA_CERT
Test de la suppression du certificat CA.

## POST_REBOOT_AFTER_CONFIG
Test du redémarrage du produit après la modification des fichiers de configs

## GET_LOG_STANDARD
Test de la récupération du fichier de logs standard.

## GET_LOG_STANDARD_BACKUP
Test de la récupération du fichier de logs standard précédent.

## GET_LOG_SYSTEM
Test de la récupération du fichier de logs système.

## GET_LOG_SYSTEM_BACKUP
Test de la récupération du fichier de logs système précédent.

## COAPS_POST_TEMPERATURE_OFFSET
Test de l'envoi des paramètres pour la température.

## COAPS_GET_TEMPERATURE_OFFSET
Test de la récupération des paramètres pour la température.

## CHECK_TEMPERATURE_OFFSET
Vérification de l'application de l'offest de température.

## COAPS_RESET_TEMPERATURE_OFFSET
Test de l'envoi des paramètres pour la température.

## COAPS_POST_HUMIDITY_OFFSET
Test de l'envoi des paramètres pour la température.

## COAPS_GET_HUMIDITY_OFFSET
Test de la récupération des paramètres pour la température.

## CHECK_HUMIDITY_OFFSET
Vérification de l'application de l'offest de température.

## COAPS_RESET_HUMIDITY_OFFSET
Test de l'envoi des paramètres pour la température.

## COAPS_GET_AIR
Test de la récupération des metrics de qualité d'air

## GET_EDGE_STATUS
Test de la récupération du status du module Edge.

## GET_EDGE_PICTURE
Test de la récupération de l'image du module Edge.

## CHECK_LOG_ERRORS
Vérification de la présence d'erreurs dans le fichier de logs depuis le dernier reboot du produit.
