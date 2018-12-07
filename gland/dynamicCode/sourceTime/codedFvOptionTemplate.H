/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     |
    \\  /    A nd           | Copyright (C) YEAR OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

Description
    Template for use with dynamic code generation of a source.
    The hook functions take the following arguments:

    codeCorrect
    (
        GeometricField<Type, fvPatchField, volMesh>& fld
    )

    codeAddSup
    (
        fvMatrix<Type}>& eqn,
        const label fieldi
    )

    constrain
    (
        fvMatrix<Type}>& eqn,
        const label fieldi
    )

    where :
        fld is the field in fieldNames
        eqn is the fvMatrix

    energySource
    {
        type            scalarCodedSource;

        active          true;
        selectionMode   all;

        scalarCodedSourceCoeffs
        {
            fieldNames      (h);
            name    sourceTime;

            codeInclude
            #{

            #};

            codeCorrect
            #{
                Pout<< "**codeCorrect**" << endl;
            #};

            codeAddSup
            #{
                const Time& time = mesh().time();
                const scalarField& V = mesh_.V();
                scalarField& heSource = eqn.source();
                heSource -= 0.1*sqr(time.value())*V;
            #};

            codeSetValue
            #{
                Pout<< "**codeSetValue**" << endl;
            #};

            // Dummy entry. Make dependent on above to trigger recompilation
            code
            #{
                #line 52 "/home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/constant/tumor/fvOptions.blood_perfusion_tumor.scalarCodedSourceCoeffs"

                #line 57 "/home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/constant/tumor/fvOptions.blood_perfusion_tumor.scalarCodedSourceCoeffs"
Pout<< "**codeCorrect**" << endl;
                #line 62 "/home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/constant/tumor/fvOptions.blood_perfusion_tumor.scalarCodedSourceCoeffs"
//scalar Tvol = 0;
            //const Time& time = mesh().time();
	    //volScalarField& T=thermo.Tmodifiable();
            const volScalarField& T = mesh_.lookupObject<volScalarField>("T");
	    //const volScalarField& Tm = mesh().thermo.T(); 
	    //volScalarField magnitudeTemp = mag(Tm);
            //Tvol = Tm.weightedAverage(mesh().V()).value();                //averageValue of the volScalarField
	    //Info << "Tvol"<< endl;
            const vectorField& C = mesh_.C();                    //List of cellcentres
	    const scalarField& V = mesh_.V();
	    const volScalarField z = T.mesh().C() & vector(1,1,1);
	    //const scalar meanT = sum(mag(Tm)*V)/sum(V);
            scalarField& hSource = eqn.source();                //defining source

	    forAll(T, i)
            {
                hSource[i] -= (37 - T[i])*48000*V[i];
		
            }
	    
            Pout << "***codeAddSup***" << endl;
                #line 87 "/home/shailesh/Niramai/Niramai_cases/with_subprocess/gland/constant/tumor/fvOptions.blood_perfusion_tumor.scalarCodedSourceCoeffs"
Pout<< "**codeSetValue**" << endl;
            #};
        }

        sourceTimeCoeffs
        {
            // Dummy entry
        }
    }

SourceFiles
    codedFvOptionTemplate.C

\*---------------------------------------------------------------------------*/

#ifndef codedFvOptionTemplate_H
#define codedFvOptionTemplate_H

#include "cellSetOption.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

namespace fv
{

/*---------------------------------------------------------------------------*\
                         A templated CodedFvOption
\*---------------------------------------------------------------------------*/

class sourceTimeFvOptionscalarSource
:
    public cellSetOption
{
public:

    //- Information about the SHA1 of the code itself
    static const char* const SHA1sum;

    //- Runtime type information
    TypeName("sourceTime");


    // Constructors

        //- Construct from patch and internal field
        sourceTimeFvOptionscalarSource
        (
            const word& name,
            const word& modelType,
            const dictionary& dict,
            const fvMesh& mesh
        );

    //- Destructor
    virtual ~sourceTimeFvOptionscalarSource();


    // Member functions

            //- Correct field
            virtual void correct
            (
                GeometricField<scalar, fvPatchField, volMesh>&
            );

            //- Explicit and implicit matrix contributions
            virtual void addSup
            (
                fvMatrix<scalar>& eqn,
                const label fieldi
            );

            //- Explicit and implicit matrix contributions for compressible
            //  equations
            virtual void addSup
            (
                const volScalarField& rho,
                fvMatrix<scalar>& eqn,
                const label fieldi
            );

            //- Set value
            virtual void constrain
            (
                fvMatrix<scalar>& eqn,
                const label fieldi
            );
};


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

} // End namespace fv

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

#endif

// ************************************************************************* //

