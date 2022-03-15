# half this shit probs isnt even needed im just too lazy to remove un needed stuff so do it ur self shii
interface=eth0
dumpdir=/root
while /bin/true; do
  pkt_old=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`
  sleep 1
  pkt_new=`grep $interface: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'`

  pkt=$(( $pkt_new - $pkt_old ))
  echo -ne "\r Interface: $interface | Live PPS: $pkt |"
   if [ $pkt -gt 400 ]; then # Max pps
    echo -e "\n`date` Attack detected Gathering Info"
  dateinfo=`date +"%d-%m-%y-%H:%M:%S"`
    tcpdump -n -s0 -c 5000 -w $dumpdir/TCPDUMP/pcap/$dateinfo.pcap # You can change this command to whatever, Dump only certain flags or whatever you want hhhhh
  tshark -r /root/TCPDUMP/pcap/$dateinfo.pcap -T fields -e ip.src > /root/TCPDUMP/report/attackingips.$dateinfo.txt
  tshark -r /root/TCPDUMP/pcap/$dateinfo.pcap -T fields -e ip.src > /root/TCPDUMP/nigga/hookinfo.txt
  tshark -r /root/TCPDUMP/pcap/$dateinfo.pcap -T fields -e ip.src > /root/TCPDUMP/extra/sortingip.txt
  tshark -r /root/TCPDUMP/pcap/$dateinfo.pcap -T fields -e tcp.dstport -e udp.dstport > /root/TCPDUMP/extra/destport.txt
  tshark -r /root/TCPDUMP/pcap/$dateinfo.pcap -T fields -e tcp.srcport -e udp.srcport > /root/TCPDUMP/extra/srcport.txt
  sort /root/TCPDUMP/extra/$dateinfo.destport.txt | uniq > /root/TCPDUMP/extra/destportsorted.txt
  sort /root/TCPDUMP/extra/sortingip.txt | uniq > /root/TCPDUMP/extra/sortedip.txt
  sort /root/TCPDUMP/extra/sortingip.txt | uniq > /root/TCPDUMP/extra/sortedip.txt
  sort /root/TCPDUMP/extra/protos.txt | uniq > /root/TCPDUMP/extra/sortedproto.txt
  sort /root/TCPDUMP/nigga/hookinfo.txt | uniq > /root/TCPDUMP/nigga/infoforfing.txt
  echo "[38;2;255;49;0m[[38;2;255;51;0mE[38;2;255;54;0mv[38;2;255;57;0me[38;2;255;60;0mn[38;2;255;63;0mt[38;2;255;66;0m][38;2;255;69;0m [38;2;255;72;0m|[38;2;255;75;0m [38;2;255;78;0m[[38;2;255;80;0mA[38;2;255;83;0mt[38;2;255;86;0mt[38;2;255;89;0ma[38;2;255;92;0mc[38;2;255;95;0mk[38;2;255;98;0mD[38;2;255;101;0me[38;2;255;104;0mt[38;2;255;107;0me[38;2;255;109;0mc[38;2;255;112;0mt[38;2;255;115;0me[38;2;255;118;0md[38;2;255;121;0m][38;2;255;124;0m [38;2;255;127;0m|[38;2;255;130;0m [38;2;255;133;0mD[38;2;255;136;0mu[38;2;255;138;0mm[38;2;255;141;0mp[38;2;255;144;0m [38;2;255;147;0mN[38;2;255;150;0ma[38;2;255;153;0mm[38;2;255;156;0me[38;2;255;159;0m [38;2;255;162;0m>[0m $dateinfo.pcap"
  echo "[38;2;255;49;0m[[38;2;255;51;0mE[38;2;255;54;0mv[38;2;255;57;0me[38;2;255;60;0mn[38;2;255;63;0mt[38;2;255;66;0m][38;2;255;69;0m [38;2;255;72;0m|[38;2;255;75;0m [38;2;255;78;0m[[38;2;255;80;0mA[38;2;255;83;0mt[38;2;255;86;0mt[38;2;255;89;0ma[38;2;255;92;0mc[38;2;255;95;0mk[38;2;255;98;0mD[38;2;255;101;0me[38;2;255;104;0mt[38;2;255;107;0me[38;2;255;109;0mc[38;2;255;112;0mt[38;2;255;115;0me[38;2;255;118;0md[38;2;255;121;0m][38;2;255;124;0m [38;2;255;127;0m|[38;2;255;130;0m [38;2;255;133;0mA[38;2;255;136;0mt[38;2;255;138;0mt[38;2;255;141;0ma[38;2;255;144;0mc[38;2;255;147;0mk[38;2;255;150;0mi[38;2;255;153;0mn[38;2;255;156;0mg[38;2;255;159;0m [38;2;255;162;0mI[38;2;255;165;0mP[38;2;255;167;0mS[38;2;255;169;0m [38;2;255;171;0mN[38;2;255;174;0ma[38;2;255;176;0mm[38;2;254;178;0me[38;2;254;180;0m [38;2;254;183;0m>[0m attackingips.$dateinfo.txt"
  echo "[38;2;255;49;0m[[38;2;255;51;0mE[38;2;255;54;0mv[38;2;255;57;0me[38;2;255;60;0mn[38;2;255;63;0mt[38;2;255;66;0m][38;2;255;69;0m [38;2;255;72;0m|[38;2;255;75;0m [38;2;255;78;0m[[38;2;255;80;0mA[38;2;255;83;0mt[38;2;255;86;0mt[38;2;255;89;0ma[38;2;255;92;0mc[38;2;255;95;0mk[38;2;255;98;0mD[38;2;255;101;0me[38;2;255;104;0mt[38;2;255;107;0me[38;2;255;109;0mc[38;2;255;112;0mt[38;2;255;115;0me[38;2;255;118;0md[38;2;255;121;0m][38;2;255;124;0m [38;2;255;127;0m|[38;2;255;130;0m [38;2;255;133;0mA[38;2;255;136;0mt[38;2;255;138;0mt[38;2;255;141;0ma[38;2;255;144;0mc[38;2;255;147;0mk[38;2;255;150;0m [38;2;255;153;0mP[38;2;255;156;0mP[38;2;255;159;0mS[38;2;255;162;0m [38;2;255;165;0m>[0m $pkt"
  echo "[38;2;255;49;0m[[38;2;255;51;0mI[38;2;255;54;0mn[38;2;255;57;0mf[38;2;255;60;0mo[38;2;255;63;0m][38;2;255;66;0m [38;2;255;69;0m [38;2;255;72;0m|[38;2;255;75;0m [38;2;255;78;0m [38;2;255;80;0m[[38;2;255;83;0mW[38;2;255;86;0me[38;2;255;89;0mb[38;2;255;92;0mH[38;2;255;95;0mo[38;2;255;98;0mo[38;2;255;101;0mk[38;2;255;104;0mP[38;2;255;107;0mo[38;2;255;109;0ms[38;2;255;112;0mt[38;2;255;115;0m][38;2;255;118;0m [38;2;255;121;0m [38;2;255;124;0m [38;2;255;127;0m|[38;2;255;130;0m [38;2;255;133;0mT[38;2;255;136;0mh[38;2;255;138;0me[38;2;255;141;0m [38;2;255;144;0ma[38;2;255;147;0mt[38;2;255;150;0mt[38;2;255;153;0ma[38;2;255;156;0mc[38;2;255;159;0mk[38;2;255;162;0m [38;2;255;165;0mh[38;2;255;167;0ma[38;2;255;169;0ms[38;2;255;171;0m [38;2;255;174;0mb[38;2;255;176;0me[38;2;254;178;0me[38;2;254;180;0mn[38;2;254;183;0m [38;2;254;185;0mp[38;2;254;187;0mo[38;2;254;189;0ms[38;2;253;192;0mt[38;2;253;194;0me[38;2;253;196;0md[38;2;253;198;0m [38;2;253;201;0mt[38;2;253;203;0mo[38;2;252;205;0m [38;2;252;207;0md[38;2;252;210;0mi[38;2;252;212;0ms[38;2;252;214;0mc[38;2;251;216;0mo[38;2;251;219;0mr[38;2;251;221;0md[38;2;251;223;0m [38;2;251;225;0mw[38;2;251;228;0me[38;2;250;230;0mb[38;2;250;232;0mh[38;2;250;234;0mo[38;2;250;237;0mo[38;2;250;239;0mk[38;2;250;241;0m.[38;2;249;243;0m [0m"
  tshark -r $dumpdir/TCPDUMP/pcap/$dateinfo.pcap -T fields -E header=y -e ip.proto -e tcp.flags -e udp.srcport -e tcp.srcport -e data > /root/TCPDUMP/info/$dateinfo.txt
   echo "Removing ACK Responces From Ip Report File.."
   sed -i 's/139.99.142.214,//g' /root/TCPDUMP/extra/sortedip.txt #replace with your server ip , this prevents your ip showing up in most frequent attacking ip (bc of ACK)
   sed -i 's/139.99.142.214//g' /root/TCPDUMP/extra/sortedip.txt #replace with your server ip , this prevents your ip showing up in most frequent attacking ip (bc of ACK)
   sed -i 's/1194/1194|OVPN/g' /root/TCPDUMP/extra/destport.txt
   sed -i 's/22/22|SSH/g' /root/TCPDUMP/extra/destport.txt
   sed -i 's/80/80|HTTP/g' /root/TCPDUMP/extra/destport.txt
   sed -i 's/443/443|HTTPS/g' /root/TCPDUMP/extra/destport.txt
   sleep 1
    python3 webhook.py /root/TCPDUMP/info/$dateinfo.txt /root/TCPDUMP/pcap/$dateinfo.pcap
    sleep 45s  && pkill -HUP -f /usr/sbin/tcpdump
  fi
done
