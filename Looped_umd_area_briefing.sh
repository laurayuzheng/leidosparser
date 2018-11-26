#!/bin/bash
set -x
if [[ $# = 0 ]]
then
  echo "Usage :"
  echo "  $0 Acid    Fix Radius(2-100)"
  echo "  $0 TTT1234 BWI 5"
else

# Set up array of airports
Airports=(JFK IAD MCO DTW ORD MSY BWI LAS SEA SFO DFW IAH BNA DEN HNL ATL LAX CLT EWR PHX MKE BOS SLC PDX MSP)

for i in `seq 1 20`; do
    for t in ${Airports[@]}; do
        Fix=$t
        Xdate=`date +%Y-%m-%d -d "2 hour"`
        Acid=$1
        Radius=5
        Msg='<?xml version="1.0" encoding="UTF-8" standalone="yes"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><ns2:AreaBriefingRequest xmlns:ns2="https://lmfsweb.afss.com/Website/schemas"><ns2:versionRequested>99991231</ns2:versionRequested><ns2:notABriefing>true</ns2:notABriefing><ns2:briefingType>NGB</ns2:briefingType><ns2:fixName><ns2:locationIdentifier>SOURCE</ns2:locationIdentifier></ns2:fixName><ns2:departureInstant>YYYY-MM-DDT23:59:00.0</ns2:departureInstant><ns2:briefingRadius>RADIUS</ns2:briefingRadius></ns2:AreaBriefingRequest></SOAP-ENV:Body></SOAP-ENV:Envelope>'

        Msg1=`echo ${Msg} | sed "s/YYYY-MM-DD/${Xdate}/g" | sed "s/SOURCE/${Fix}/g" | sed "s/ACID/${Acid}/g" | sed "s/RADIUS/${Radius}/g" `

        echo ==================
        echo $Msg1
        echo ==================

        a='briefing'
        #can be modified to change file names too
        TMP_FILE=XML_Data/"$a$t".xml
        /usr/bin/curl -k -A "Mozilla/5.0" -i -c cookies/cookies. -H 'Content-Type: text/xml' -u "leidos.umd.project@leidos.com:L3!D0s2018" --data "${Msg1}" "https://www.elabs.testafss.net/Website2/ws"  > $TMP_FILE
        sed -i '1,18d' $TMP_FILE
        sed -i 's/<SOAP-ENV:Envelope xmlns:SOAP-ENV="http:\/\/schemas.xmlsoap.org\/soap\/envelope\/"><SOAP-ENV:Header\/><SOAP-ENV:Body>//g' $TMP_FILE
        sed -i 's/<\/SOAP-ENV:Body><\/SOAP-ENV:Envelope>//g' $TMP_FILE
        # sleep 30s #maybe longer
    done
    sleep 6h
    echo$i
done


fi
