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

\*---------------------------------------------------------------------------*/

#include "codedFvOptionTemplate.H"
#include "addToRunTimeSelectionTable.H"
#include "fvPatchFieldMapper.H"
#include "volFields.H"
#include "surfaceFields.H"
#include "unitConversion.H"
#include "fvMatrix.H"

//{{{ begin codeInclude
#line 51 "/home/shailesh/Niramai/Niramai_cases/with_subprocess_no_tumor/gland/constant/tissue/fvOptions.blood_perfusion_tissue.scalarCodedSourceCoeffs"

//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

namespace fv
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    // dynamicCode:
    // SHA1 = 07ffd593991730870ff18e5813d3da8346b17cda
    //
    // unique function name that can be checked if the correct library version
    // has been loaded
    void sourceTime_07ffd593991730870ff18e5813d3da8346b17cda(bool load)
    {
        if (load)
        {
            // code that can be explicitly executed after loading
        }
        else
        {
            // code that can be explicitly executed before unloading
        }
    }
}

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

//makeRemovablePatchTypeField
//(
//    fvPatch,
//    sourceTimeFvOptionscalarSource
//);
defineTypeNameAndDebug(sourceTimeFvOptionscalarSource, 0);
addRemovableToRunTimeSelectionTable
(
    option,
    sourceTimeFvOptionscalarSource,
    dictionary
);


const char* const sourceTimeFvOptionscalarSource::SHA1sum =
    "07ffd593991730870ff18e5813d3da8346b17cda";


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

sourceTimeFvOptionscalarSource::
sourceTimeFvOptionscalarSource
(
    const word& name,
    const word& modelType,
    const dictionary& dict,
    const fvMesh& mesh
)
:
    cellSetOption(name, modelType, dict, mesh)
{
    if (false)
    {
        Info<<"construct sourceTime sha1: 07ffd593991730870ff18e5813d3da8346b17cda"
            " from components\n";
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

sourceTimeFvOptionscalarSource::
~sourceTimeFvOptionscalarSource()
{
    if (false)
    {
        Info<<"destroy sourceTime sha1: 07ffd593991730870ff18e5813d3da8346b17cda\n";
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void sourceTimeFvOptionscalarSource::correct
(
    GeometricField<scalar, fvPatchField, volMesh>& fld
)
{
    if (false)
    {
        Info<<"sourceTimeFvOptionscalarSource::correct()\n";
    }

//{{{ begin code
    #line 56 "/home/shailesh/Niramai/Niramai_cases/with_subprocess_no_tumor/gland/constant/tissue/fvOptions.blood_perfusion_tissue.scalarCodedSourceCoeffs"
Pout<< "**codeCorrect**" << endl;
//}}} end code
}


void sourceTimeFvOptionscalarSource::addSup
(
    fvMatrix<scalar>& eqn,
    const label fieldi
)
{
    if (false)
    {
        Info<<"sourceTimeFvOptionscalarSource::addSup()\n";
    }

//{{{ begin code
    #line 61 "/home/shailesh/Niramai/Niramai_cases/with_subprocess_no_tumor/gland/constant/tissue/fvOptions.blood_perfusion_tissue.scalarCodedSourceCoeffs"
scalar Tvol = 0;
            //const Time& time = mesh().time();
            const volScalarField& Tm = mesh_.lookupObject<volScalarField>("T"); 
            Tvol = Tm.weightedAverage(mesh_.V()).value();                //averageValue of the volScalarField
            const vectorField& C = mesh_.C();                    //List of cellcentres
	    const scalarField& V = mesh_.V();
            scalarField& hSource = eqn.source();                //defining source
            forAll(C, i)
            {
                hSource[i] -= (37 - Tvol)*800*V[i];
            }
            Pout << "***codeAddSup***" << endl;
//}}} end code
}


void sourceTimeFvOptionscalarSource::addSup
(
    const volScalarField& rho,
    fvMatrix<scalar>& eqn,
    const label fieldi
)
{
    if (false)
    {
        Info<<"sourceTimeFvOptionscalarSource::addSup()\n";
    }

//{{{ begin code
    #line 61 "/home/shailesh/Niramai/Niramai_cases/with_subprocess_no_tumor/gland/constant/tissue/fvOptions.blood_perfusion_tissue.scalarCodedSourceCoeffs"
scalar Tvol = 0;
            //const Time& time = mesh().time();
            const volScalarField& Tm = mesh_.lookupObject<volScalarField>("T"); 
            Tvol = Tm.weightedAverage(mesh_.V()).value();                //averageValue of the volScalarField
            const vectorField& C = mesh_.C();                    //List of cellcentres
	    const scalarField& V = mesh_.V();
            scalarField& hSource = eqn.source();                //defining source
            forAll(C, i)
            {
                hSource[i] -= (37 - Tvol)*800*V[i];
            }
            Pout << "***codeAddSup***" << endl;
//}}} end code
}


void sourceTimeFvOptionscalarSource::constrain
(
    fvMatrix<scalar>& eqn,
    const label fieldi
)
{
    if (false)
    {
        Info<<"sourceTimeFvOptionscalarSource::constrain()\n";
    }

//{{{ begin code
    #line 77 "/home/shailesh/Niramai/Niramai_cases/with_subprocess_no_tumor/gland/constant/tissue/fvOptions.blood_perfusion_tissue.scalarCodedSourceCoeffs"
Pout<< "**codeSetValue**" << endl;
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam

} // End namespace fv
// ************************************************************************* //

