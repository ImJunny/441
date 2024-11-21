    def next_generation(self, population):
        selected = self.select(len(population), population)
        newGen = []
        for chrom1 in population:
            #crossover chrom1 with another chrom from self.select for better crossovers
            chrom2 = random.choice(selected)
            tempChrom = self.crossover(chrom1,chrom2)
            tempChrom = self.mutate(tempChrom)
            newGen.append(tempChrom)
        return newGen