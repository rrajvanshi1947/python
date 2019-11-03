# # # Add any imports you need here
# import datetime
# class WAL:
#     def __init__(self, a):
#         # TODO
#         self.arr = [None]*len(a)
#         for i in range(len(a)):
#             parse = a[i].split('|')
#             if parse[1] == 0:
#                 parse[1] = 'INSERT'
#             elif parse[1] == 1:
#                 parse[1] = 'UPSERT'
#             elif parse[1] == 2:
#                 parse[1] = 'DELETE'
#                 parse[5] = ''
#                 self.arr[i] = str(parse[0]) + '|' + str(parse[1]) + '|' + str(parse[3])
#                 continue
#             self.arr[i] = str(parse[0]) + '|' + str(parse[1]) + '|' + str(parse[3]) + '|' + str(parse[5])


#     def get_events(self):
#         """ Retrieve all events contained within the WAL as their string values in time order
#         DML Event String Format: "<epoch_milli>|<message_name>|<key>|<value>"

#         Returns
#         -------
#         list(str): a time-ordered list of DML Event strings
#         """
#         return self.arr


#         return list()

# s = 1236472051807/1000.0
# print(datetime.datetime.fromtimestamp(s))



public static class WAL {
   /**
    * Construct the WAL
    * @param input the raw binary WAL
    */
   public ArrayList<String> events=new ArrayList<>();
   public WAL(byte[] input) {
       // TODO
       int i=0;
       while(i<input.length){
           long epochMilli=0;
           int messageType;
           String messageCode;
           int keyLength=0;
           String key="";
           int valueLength=0;
           String value="";
           for(int j=0; j<8; j++){
               epochMilli += ((long) input[i++] & 0xffL) << (8 * j);
           }
           messageType=input[i++];
           if(messageType==0){
               messageCode="INSERT";
           }
           else if(messageType==1){
               messageCode="UPSERT";
           }
           else{
               messageCode="DELETE";
           }
           for(int j=0; j<2; j++){
               keyLength += ((int) input[i++] & 0xffL) << (8 * j);
           }
           byte[] keyArray=new byte[8];
           System.arraycopy(input, i, keyArray, 0, 8);
           try{
               key = new String(keyArray, "US-ASCII");
           }
           catch (Exception e){
               e.printStackTrace();
           }
           i=i+8;

           for(int j=0; j<2; j++){
               valueLength += ((int) input[i++] & 0xffL) << (8 * j);
           }
           byte[] valueArray=new byte[8];
           System.arraycopy(input, i, valueArray, 0, 8);
           try{
               value = new String(valueArray, "US-ASCII");
           }
           catch (Exception e){
               e.printStackTrace();
           }
           i=i+8;
           StringBuilder event=new StringBuilder();
           event=event.append(epochMilli).append("\\|").append(messageCode).append("\\|").append(key).append("\\|").append(value);
           events.add(event.toString());
          
       }
   }

   /**
    * Retrieve all events contained within the WAL as their string values in time order
    * DML Event String Format: "<epoch_milli>|<message_name>|<key>|<value>"
    *
    * @return a time-ordered sequence of DML Event strings
    */
   public ArrayList<String> getEvents() {
       // TODO
       return events;
   }
}
