interface MajorCredits {
    credit: number;
    _brand: 'major';
};

interface MinorCredits {
    credit: number;
    _brand: "minor";
};

function sumMajorCredits(subject1: MajorCredits, subject2: MajorCredits): number {
    return subject1.credit + subject2.credit;
}

function sumMinorCredits(subject1: MinorCredits, subject2: MinorCredits): number {
    return subject1.credit + subject2.credit; 
}