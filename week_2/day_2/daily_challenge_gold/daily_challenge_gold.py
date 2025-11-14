from random import randint, random

class Gene:
    def __init__(self):
        self.state = randint(0, 1)

    def mutate(self):
        self.state = randint(0, 1)

class Chromosome:
    def __init__(self, genes = None):
        if genes is None:
            genes = []
        self.genes = []
        for gene in genes:
            if isinstance(gene, Gene):
                self.genes.append(gene)
        if len(self.genes) < 10:
            self.genes.extend(self.__generate_genes(10 - len(self.genes)))

    def __generate_genes(self, count):
        return [Gene() for _ in range(count)]
    
    def mutate(self):
        for gene in self.genes:
            gene.mutate()

class DNA:
    def __init__(self, chromosomes = None):
        if chromosomes is None:
            chromosomes = []
        self.chromosomes = []
        for chromosome in chromosomes:
            if isinstance(chromosome, Chromosome):
                self.chromosomes.append(chromosome)
        if len(chromosomes) < 10:
            self.chromosomes.extend(self.__generate_chromosomes(10 - len(self.chromosomes)))

    def __generate_chromosomes(self, count):
        return [Chromosome() for _ in range(count)]
    
    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

class Organism:
    def __init__(self, dna, env = 0.5):
        if not isinstance(dna, DNA):
            raise Exception('Must be DNA object!')
        self.generations = 1
        self.dna = dna
        self.env = env

    def mutate(self):
        for chromosome in self.dna.chromosomes:
            if random() < self.env:
                chromosome.mutate()
        self.generations += 1

    def mutate_until_1(self):
        found = False
        while not found:
            zero_exists = False
            for chromosome in self.dna.chromosomes:
                for gene in chromosome.genes:
                    if gene.state == 0:
                        zero_exists = True
                        break
                if zero_exists:
                    break
            if zero_exists == False:
                found = True
            else:
                self.mutate()
            self.generations += 1
                
genes1 = [Gene() for _ in range(10)]
genes2 = [Gene() for _ in range(10)]

chrom1 = Chromosome(genes1)
chrom2 = Chromosome(genes2)

dna = DNA([chrom1, chrom2])

organism = Organism(dna, env=1)

print("Initial gene states:")
for i, chrom in enumerate(organism.dna.chromosomes):
    print(f"Chromosome {i+1}: {[gene.state for gene in chrom.genes]}")

# organism.mutate_until_1()
organism.mutate()

print("After mutate:")
for i, chrom in enumerate(organism.dna.chromosomes):
    print(f"Chromosome {i+1}: {[gene.state for gene in chrom.genes]}")

print(f"Generations: {organism.generations}")
