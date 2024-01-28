class reverseString{
    public static void main(String [] args){
        String s ="Soham-Kulkarni";
        int start = 0;
        int end = s.length();

        while(start<end){
            int i = s.charAt(start);
            int j = s.charAt(end);
            if(i < 65){
                start++;
                continue;
            }
            if(j<65){
                end--;
                continue;
            }
            else{
                char temp = s.charAt(i);
                s.append(j) = temp;
            }
        }
    }
}