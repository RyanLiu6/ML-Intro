import time
import Levenshtein as lev


class packageChecker:
    def checkUser(self, inputStr, userInfo):
        # Find where query is in the inputStr
        name = userInfo["Name"].lower()
        addr = userInfo["Address"].lower()

        return any(self.checkQuery(inputStr, name, addr))


    def checkPackage(self, inputStr, packageInfo):
        query = []

        currDate = int(time.time())
        for package in packageInfo:
            pkgDate = package["Delivery Date"]

            time_tuple = time.strptime(pkgDate + " 23:59:59", "%m/%d/%Y %H:%M:%S")
            expDate = time.mktime(time_tuple)
            if currDate <= expDate:
                query.append(package["Tracking Info"])

        return any(self.checkQuery(inputStr, *query))


    def checkQuery(self, strList, *queries):
        results = [False for _ in queries]
        print(queries)
        for line in strList:
            for index, query in enumerate(queries):
                if not results[index]:
                    results[index] = lev.ratio(query, line) > 0.5

        return results
