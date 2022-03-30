//SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract newvote{

    

    //create map
 
    mapping(uint256=>bool ) public CandidateIdtoBool;    
    //CandidateIdtoBool[_candidateId] = true;

    mapping(uint256=>string ) public CandidateIdtoName;

    mapping(uint256=> uint256) public partyIdToCandidateId;

    mapping(uint256=> uint256) public candidateIdToVotes;


    //name will be stored in memory
    
    function addCandidate(string memory _candidateName, uint256 _candidateId, uint256  _partyId) public {
        // candidate.push(Candidate({votes : 0, candidateName:_candidateName,candidateId: _candidateId}));
        if (validCandidate(_candidateId) ) { revert("Not a valid canditate ");}
        else{
        CandidateIdtoName[_candidateId] = _candidateName;
        CandidateIdtoBool[_candidateId] = true;
        partyIdToCandidateId[_partyId] = _candidateId;
        }
    }

    //checking if candidate is valid

    function validCandidate(uint256 _candidateId) public view returns(bool){

            if(CandidateIdtoBool[_candidateId]){
                return true;
            }
            else{
                return false;
            }
        
    }

    // voting for a candidate
    function voteForCandidate(uint256 candidateId) public  {
        if (validCandidate(candidateId) ) {
            candidateIdToVotes[candidateId] += 1;
        }
        else{
            revert("Not a valid canditate ");
        } 
    }

    function get  (uint256 candidateId) public view returns(uint256){
         if (validCandidate(candidateId) ) {
            return candidateIdToVotes[candidateId];
        }
        else{
            revert("Not a valid canditate ");
        }          
  }

      function getVote  (uint256 candidateId) public view returns(uint256){
         
            return candidateIdToVotes[candidateId];
        
  
  }


}