*** Settings ***
Resource    ../keywords/keywords_coaps.robot
Resource    ../keywords/keywords_json.robot
# Library     DateTime

Suite Setup    COAPS_INIT    ${ble_device_name}
Suite Teardown    COAPS_CLOSE_CONNECTION

*** Variables ***
${ble_device_name}=    Legrand_pr_F8DC
${output_folder}=    ${CURDIR}/results/responses
${version_txt_filepath}=    ${CURDIR}/resources/version.txt

*** Keywords ***
POST_EMPTY_PAYLOAD
    [Documentation]
    ...    Template pour exécuter une requête POST avec un paylaod vide sur toutes les routes voulues en argument.
    [Arguments]    ${route}    ${expected_response_code}
    COAPS_POST    ${route}    \    ${expected_response_code}

*** Test Cases ***
LOG_VARIABLES
    [Documentation]
    ...    Simple affichage des variables pour s'assurer qu'on utilise les bonnes valeurs pour le déroulement des tests.
    Log To Console    \nble_device_name : ${ble_device_name}
    Log To Console    output_folder : ${output_folder}
    Log To Console    version_txt_filepath : ${version_txt_filepath}
    

# ======================================================
#                      INVALID
# ======================================================
GET_INVALID_ROUTE
    [Documentation]
    ...    Tests de requêtes GET sur des routes invalides.
    COAPS_GET    v1/non-existing    404     # Route non existante
    COAPS_GET    v2/status    404           # Route existante avec v2
    COAPS_GET    v1/reboot    404           # Route existante mais pas en GET
    COAPS_GET    before/v1/status    404    # Route existante avec un niveau avant incorrect
    COAPS_GET    v1/status/after    404     # Route existante avec un niveau après incorrect

POST_INVALID_ROUTE
    [Documentation]
    ...    Tests de requêtes POST sur des routes invalides.
    COAPS_POST    v1/non-existing    \    404     # Route non existante
    COAPS_POST    v2/reboot    \    404           # Route existante avec v2
    COAPS_POST    v1/status    \    404           # Route existante mais pas en POST
    COAPS_POST    before/v1/reboot    \    404    # Route existante avec un niveau avant incorrect
    COAPS_POST    v1/reboot/after    \    404     # Route existante avec un niveau après incorrect

# POST_FILE_INVALID_ROUTE
#     [Documentation]
#     ...    Test du temps de réponse d'une requête POST avec un fichier sur une route inexistante.
#     ${before}=    Get Current Date    exclude_millis=${True}
#     COAPS_POST_BINARY_FILE_CONTENT    v1/non-existing    ${CURDIR}/resources/40Ko_bin_file    404    # Route inexistante avec fichier de 40Ko
#     ${after}=    Get Current Date    exclude_millis=${True}
#     Log    ${before}
#     Log    ${after}
#     ${elapsed}=    Subtract Date From Date    ${after}    ${before}
#     Should Be True    ${elapsed}<${10}

DELETE_INVALID_ROUTE
    [Documentation]
    ...    Tests de requêtes DELETE sur des routes invalides.
    COAPS_DELETE    v1/non-existing    404                    # Route non existante
    COAPS_DELETE    v2/configuration/network    404           # Route existante avec v2
    COAPS_DELETE    v1/status    404                          # Route existante mais pas en DELETE
    COAPS_DELETE    before/v1/configuration/network    404    # Route existante avec un niveau avant incorrect
    COAPS_DELETE    /v1/configuration/network/after    404    # Route existante avec un niveau après incorrect

POST_EMPTY_PAYLOAD_EVERY_POST_ROUTE
    [Documentation]
    ...    Tests de requêtes POST avec des payloads vides.
    [Template]    POST_EMPTY_PAYLOAD
    v1/configuration/network    400
    v1/configuration/mqtt    400
    v1/configuration/broker_metrics_0    404
    v1/configuration/ca_cert/0    400
    v1/configuration/user_psk    406
    v1/configuration/update    404


# ======================================================
#                      ACTIVITY
# ======================================================
GET_STATUS
    [Documentation]
    ...    Test de récupération des différentes versions firmwares et du statut de l'appareil.
    COAPS_GET    v1/status    205

CHECK_VERSION
    [Documentation]
    ...    Test de comparaison des différentes versions firmwares à celles attendues.
    ...    Les versions sont comparées à celle contenues dans le fichier version.txt de l'artefact.
    ${response_code}    ${response_payload}=    COAPS_GET_RETURN_RESPONSE    v1/status
    CHECK_VERSION    ${response_payload}    ${version_txt_filepath}

GET_SWAGGER
    [Documentation]
    ...    Test de la route permettant de récupérer le swagger.
    COAPS_GET    v1/swagger    205
    
    
# ======================================================
#                      NETWORK
# ======================================================
POST_CONFIGURATION_NETWORK
    [Documentation]
    ...    Test de l'envoi d'une configuration réseau.
    ${network_configuration}=    CREATE_CONFIGURATION_NETWORK    False    192.168.20.2    255.255.255.0    192.168.20.1    192.168.20.1    \
    COAPS_POST    v1/configuration/network    ${network_configuration}    205

GET_CONFIGURATION_NETWORK
    [Documentation]
    ...    Test de la récupération de la configuration réseau.
    COAPS_GET    v1/configuration/network    205

CHECK_CONFIGURATION_NETWORK
    [Documentation]
    ...    Test de comparaison de la configuration réseau à celle attendue.
    ...    La configuration est comparée à celle envoyée précédemment.
    ${response_code}    ${response_payload}=    COAPS_GET_RETURN_RESPONSE    v1/configuration/network
    CHECK_CONFIGURATION_NETWORK    ${response_payload}    dhcp=False    address=192.168.20.2    netmask=255.255.255.0    gateway=192.168.20.1    dns=192.168.20.1

DELETE_CONFIGURATION_NETWORK
    [Documentation]
    ...    Test de la suppression de la configuration réseau.
    COAPS_DELETE    v1/configuration/network    202

GET_CONFIGURATION_NETWORK_2
    [Documentation]
    ...    Test de la récupération de la configuration réseau après suppression de celle-ci.
    COAPS_GET    v1/configuration/network    205

DELETE_CONFIGURATION_NETWORK_2
    [Documentation]
    ...    Test de la suppression de la configuration réseau avec aucune configuration présente.
   COAPS_DELETE    v1/configuration/network    404

CHECK_CONFIGURATION_NETWORK_2
    [Documentation]
    ...    Test de comparaison de la configuration réseau à celle attendue.
    ...    La configuration est comparée à celle envoyée précédemment.
    ${response_code}    ${response_payload}=    COAPS_GET_RETURN_RESPONSE    v1/configuration/network
    CHECK_CONFIGURATION_NETWORK    ${response_payload}    dhcp=True


# ======================================================
#                        MQTT
# ======================================================
POST_CONFIGURATION_MQTT
    [Documentation]
    ...    Test de l'envoi d'une configuration mqtt.
    # ${mqtt_configuration}=    CREATE_CONFIGURATION_MQTT    True    192.168.20.72    ActivityBPLocal    \    \    ActivityBPLocal    False    0    1883
    ${mqtt_configuration}=    CREATE_CONFIGURATION_MQTT    True    10.2.44.183    Activity_45    admin    password    Activity_45    False    0    8883
    COAPS_POST    v1/configuration/mqtt    ${mqtt_configuration}    205
        
GET_CONFIGURATION_MQTT
    [Documentation]
    ...    Test de la récupération de la configuration mqtt.
    COAPS_GET    v1/configuration/mqtt    205

DELETE_CONFIGURATION_MQTT
    [Documentation]
    ...    Test de suppression de la configuration mqtt.
    COAPS_DELETE    v1/configuration/mqtt    202

GET_CONFIGURATION_MQTT_2
    [Documentation]
    ...    Test de la récupération de la configuration mqtt après suppression de celle-ci.
    COAPS_GET    v1/configuration/mqtt    404
        
DELETE_CONFIGURATION_MQTT_2
    [Documentation]
    ...    Test de la suppression de la configuration mqtt avec aucune configuration présente.
    COAPS_DELETE    v1/configuration/mqtt    404


# ======================================================
#                      BROKERS
# ======================================================
POST_METRICS_BROKER_0
    [Documentation]
    ...    Test de l'envoi d'une configuration d'envoi de valeurs des capteurs en mqtt.
    ${metrics_broker_configuration}=    CREATE_CONFIGURATION_BROKER_SAME_FOR_ALL_METRICS    False    60000
    COAPS_POST    v1/configuration/metrics_broker_0    ${metrics_broker_configuration}    205

GET_METRICS_BROKER_0
    [Documentation]
    ...    Test de la récupération de la configuration d'envoi de valeurs des capteurs en mqtt.
    COAPS_GET    v1/configuration/metrics_broker_0    205
        
DELETE_METRICS_BROKER_0
    [Documentation]
    ...    Test de la suppression de la configuration d'envoi de valeurs des capteurs en mqtt.
    COAPS_DELETE    v1/configuration/metrics_broker_0    202
        
GET_METRICS_BROKER_0_2
    [Documentation]
    ...    Test de la récupération de la configuration d'envoi de valeurs des capteurs en mqtt après suppression de celle-ci.
    COAPS_GET    v1/configuration/metrics_broker_0    404

DELETE_METRICS_BROKER_0_2
    [Documentation]
    ...    Test de la suppression de la configuration d'envoi de valeurs des capteurs en mqtt avec aucune configuration présente.
    COAPS_DELETE    v1/configuration/metrics_broker_0    404


# ======================================================
#                     CERTIFICATES
# ======================================================
POST_CA_CERT
    [Documentation]
    ...    Test de l'envoi du certificat CA.
    COAPS_POST_BINARY_FILE_CONTENT    v1/configuration/ca_cert/0    ${CURDIR}/resources/certificates/CA 1/ca.der    205
    
DELETE_CA_CERT
    [Documentation]
    ...    Test de la suppression du certificat CA.
    COAPS_DELETE    v1/configuration/ca_cert/0    202

POST_REBOOT_AFTER_CONFIG
    [Documentation]
    ...    Test du redémarrage du produit après la modification des fichiers de configs
    COAPS_POST    v1/reboot    \    205
    COAPS_CLOSE_CONNECTION
    Sleep    30
    COAPS_INIT    ${ble_device_name}


# ======================================================
#                        LOGS
# ======================================================
GET_LOG_STANDARD
    [Documentation]
    ...    Test de la récupération du fichier de logs standard.
    [Tags]    Logs
    COAPS_GET    v1/log/standard    205    ${output_folder}/log_standard.txt
    
GET_LOG_STANDARD_BACKUP
    [Documentation]
    ...    Test de la récupération du fichier de logs standard précédent. 
    [Tags]    Logs
    COAPS_GET    v1/log/standard_backup    205    ${output_folder}/log_standard_backup.txt
    
GET_LOG_SYSTEM
    [Documentation]
    ...    Test de la récupération du fichier de logs système.
    [Tags]    Logs
    COAPS_GET    v1/log/system    205    ${output_folder}/log_system.txt
    
GET_LOG_SYSTEM_BACKUP
    [Documentation]
    ...    Test de la récupération du fichier de logs système précédent.
    [Tags]    Logs
    COAPS_GET    v1/log/system_backup    404    ${output_folder}/log_system_backup.txt


# ======================================================
#                       SENSORS
# ======================================================
COAPS_POST_TEMPERATURE_OFFSET
    [Documentation]
    ...    Test de l'envoi des paramètres pour la température.
    ${temperature_offset}=    CREATE_SENSORS_TEMPERATURE_PAYLOAD    0
    COAPS_POST    v1/sensors/temperature    ${temperature_offset}    205
    ${temperature_offset}=    CREATE_SENSORS_TEMPERATURE_PAYLOAD    -5
    COAPS_POST    v1/sensors/temperature    ${temperature_offset}    205
    ${temperature_offset}=    CREATE_SENSORS_TEMPERATURE_PAYLOAD    10
    COAPS_POST    v1/sensors/temperature    ${temperature_offset}    205

COAPS_GET_TEMPERATURE_OFFSET
    [Documentation]
    ...    Test de la récupération des paramètres pour la température.
    COAPS_GET    v1/sensors/temperature    205

CHECK_TEMPERATURE_OFFSET
    [Documentation]
    ...    Vérification de l'application de l'offest de température.
    ${response_code}    ${response_payload}=    COAPS_GET_RETURN_RESPONSE    v1/sensors/temperature
    CHECK_SENSORS_TEMPERATURE    ${response_payload}    10

COAPS_RESET_TEMPERATURE_OFFSET
    [Documentation]
    ...    Test de l'envoi des paramètres pour la température.
    ${temperature_offset}=    CREATE_SENSORS_TEMPERATURE_PAYLOAD    0
    COAPS_POST    v1/sensors/temperature    ${temperature_offset}    205

COAPS_POST_HUMIDITY_OFFSET
    [Documentation]
    ...    Test de l'envoi des paramètres pour la température.
    ${humidity_offset}=    CREATE_SENSORS_HUMIDITY_PAYLOAD    0
    COAPS_POST    v1/sensors/humidity    ${humidity_offset}    205
    ${humidity_offset}=    CREATE_SENSORS_HUMIDITY_PAYLOAD    -5
    COAPS_POST    v1/sensors/humidity    ${humidity_offset}    205
    ${humidity_offset}=    CREATE_SENSORS_HUMIDITY_PAYLOAD    10
    COAPS_POST    v1/sensors/humidity    ${humidity_offset}    205

COAPS_GET_HUMIDITY_OFFSET
    [Documentation]
    ...    Test de la récupération des paramètres pour la température.
    COAPS_GET    v1/sensors/humidity    205

CHECK_HUMIDITY_OFFSET
    [Documentation]
    ...    Vérification de l'application de l'offest de température.
    ${response_code}    ${response_payload}=    COAPS_GET_RETURN_RESPONSE    v1/sensors/humidity
    CHECK_SENSORS_HUMIDITY    ${response_payload}    10

COAPS_RESET_HUMIDITY_OFFSET
    [Documentation]
    ...    Test de l'envoi des paramètres pour la température.
    ${humidity_offset}=    CREATE_SENSORS_HUMIDITY_PAYLOAD    0
    COAPS_POST    v1/sensors/humidity    ${humidity_offset}    205

COAPS_GET_AIR
    [Documentation]
    ...    Test de la récupération des metrics de qualité d'air
    COAPS_GET    v1/sensors/air    205

GET_EDGE_STATUS
    [Documentation]
    ...    Test de la récupération du status du module Edge.
    COAPS_GET    v1/sensors/pcm/status    205

GET_EDGE_PICTURE
    [Documentation]
    ...    Test de la récupération de l'image du module Edge.
    COAPS_GET    v1/sensors/pcm/picture    205    #TODO: Enregistrer l'image

CHECK_LOG_ERRORS
    [Documentation]
    ...    Vérification de la présence d'erreurs dans le fichier de logs depuis le dernier reboot du produit.
    COAPS_GET    v1/log/standard    205    ${output_folder}/log_standard.txt
    CHECK_ERRORS_IN_LOG_FILE    ${output_folder}/log_standard.txt


# ======================================================
#                         PSK
# ======================================================
# POST_USER_PSK
#     [Documentation]
#     ...    Test de l'envoi de la clé psk utilisateur.
#     COAPS_POST    v1/configuration/user_psk    0123456789ABCDEF0123456789ABCDEF    205