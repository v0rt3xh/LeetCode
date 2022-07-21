'''
0721 Accounts Merge
Hashtable + union find
'''
class UnionFind:
    '''
    UnionFind structure
    '''
    def __init__(self, num_of_element):
        self.parent = list(range(num_of_element))
        
    def _find(self, node):
        if (self.parent[node] != node):
            self.parent[node] = self._find(self.parent[node])
        return self.parent[node]
    
    def _union(self, node1, node2):
        self.parent[self._find(node2)] = self._find(node1)        

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Then, critical components:
        # Two hash tables
        # We use unionfind w.r.t email address.
        # First, need an node index for email address
        # Second, when retrieving, we need the corresponding account
        emailToNode = dict()
        emailToName = dict()
        # init
        for account in accounts:
            accountName = account[0]
            for email in account[1:]:
                if email not in emailToNode:
                    emailToNode[email] = len(emailToNode)
                    emailToName[email] = accountName
                    
        unionfind = UnionFind(len(emailToNode))
        for account in accounts:
            # Union the email with in one account
            firstNode = emailToNode[account[1]]
            for email in account[2:]:
                unionfind._union(firstNode, emailToNode[email])
        
        # retrieve the email
        nodeToEmails = collections.defaultdict(list)
        for email, node in emailToNode.items():
            node = unionfind._find(node)
            nodeToEmails[node].append(email)
        
        # Set into output format
        result = list()
        for emails in nodeToEmails.values():
            result.append([emailToName[emails[0]]] + sorted(emails))
        return result