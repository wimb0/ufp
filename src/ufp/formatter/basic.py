from .base import BaseFormatter
from prettytable import PrettyTable

class BasicSrcDstActionFormatter(BaseFormatter):
    """
    Basic formatter which displays source and destination pairs as
    well as the resulting action.
    """
    def format(self):
        if self.options.table:
            table = PrettyTable()
            table.field_names = ['Date', 'Protocol', 'Source IP', 'Destination IP', 'Source Port', 'Destination Port', 'Action']
        
        for line in self.entries:
            if self.options.reverse_dns:
                srckey = hash(line.src)
                if srckey not in self.hostname_cache:
                    src = line.ip_to_hostname(line.src)
                    self.hostname_cache[srckey] = src
                else:
                    src = self.hostname_cache[srckey]

                dstkey = hash(line.dst)
                if dstkey not in self.hostname_cache:
                    dst = line.ip_to_hostname(line.dst)
                    self.hostname_cache[dstkey] = dst
                else:
                    dst = self.hostname_cache[dstkey]
            else:
                src = line.src
                dst = line.dst

            if src is None:
                src = line.src
            if dst is None:
                dst = line.dst
                
            if self.options.table:
                table.add_row([line.date.strftime('%Y-%m-%d %H:%M:%S'), line.get_proto(), src, dst, line.spt, line.dpt, self.get_action_repr(line)])
            else:
                print("{date:20} {proto:10} SRC: {srcip:60}  DST: "
                      "{dstip:60} SPT: {spt:<8} DPT: {dpt:<8} ACTION: "
                      "{action}"
                      .format(date=line.date.strftime('%Y-%m-%d %H:%M:%S'),
                              proto=line.get_proto(), srcip=src,
                              dstip=dst, spt=line.spt, dpt=line.dpt,
                              action=self.get_action_repr(line)))
        if self.options.table:
            print(table)
