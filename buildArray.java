class buildArray {
    public static void main(String[] args) {
        int [] nums= {0,5,1,2,3,4};
        int [] ans = new int[nums.length];
        for(int i=0; i< ans.length; i++){
            ans[i] = nums[nums[i]];
        }
        for(int i=0; i<ans.length; i++){
            System.out.println(ans[i]);
        }
    }
    
}