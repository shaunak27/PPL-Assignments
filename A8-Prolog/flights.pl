airport(toronto,50,60).
airport(madrid,75,45).
airport(malaga,50,30).
airport(london,75,80).
airport(paris,50,60).
airport(toulouse,40,30).
airport(valencia,40,20).
airport(barcelona,40,30).


flight(toronto,london,united,650,420).
flight(toronto,london,air_canada,500,360).
flight(toronto,madrid,air_canada,900,480).
flight(toronto,madrid,united,950,540).
flight(toronto,madrid,iberia,800,450).
flight(london,barcelona,iberia,220,240).
flight(barcelona,madrid,air_canada,100,60).
flight(barcelona,madrid,iberia,120,65).
flight(barcelona,valencia,iberia,110,75).
flight(madrid,valencia,iberia,40,50).
flight(madrid,malaga,iberia,50,30).
flight(malaga,valencia,iberia,80,120).
flight(paris,toulouse,united,40,30).





divide(A,B,D,E,A - B) :- flight(A,B,C,D,E).
divide(A,B,D + R,E + T,A - Y) :- flight(A,Z,C,D,E) ; divide(Z,B,R,T,Y).

findFlights(A,B,C,D,E) :- divide(A,B,C,D,E) ; divide(B,A,C,D,E).



airport(C,T,D) :- airport(C,T,D).


isFlight(A,B) :- flight(A,B,C,D,E) ; flight(B,A,C,D,E).



cheap(A,B,R) :- flight(A,B,C,D<400 ,E) ; flight(A,B,R,G,H).


 
checkExistence(A,B,C,D) :- flight(A,B,C,F,E)  -> flight(A,B,D,G,H) ; flight(B,A,C,F,E)  -> flight(B,A,D,G,H).
