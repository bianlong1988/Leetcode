    def simplifyPath(self, path: str) -> str:
        res = []
        path_list = path.split('/')
        # print (path_list)
        for p in path_list:
            if len(p) != 0:
                if p == '..' :
                    if len(res) != 0:
                        res.pop()
                elif p == '.':
                    continue
                else:
                    res.append(p)
        return '/' + '/'.join(res)    