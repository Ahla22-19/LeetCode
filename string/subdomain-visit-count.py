class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
       
        ans=[]
        count = defaultdict(int)

        for domain_entry in cpdomains:
            key, value = domain_entry.split()  
            key = int(key) 
            
            subdomains = value.split('.')  
            
            for i in range(len(subdomains)):  
                subdomain_str = ".".join(subdomains[i:])  
                count[subdomain_str] += key 

        for j,k in count.items():
            ans.append(f"{k} {j}")
            
        return ans