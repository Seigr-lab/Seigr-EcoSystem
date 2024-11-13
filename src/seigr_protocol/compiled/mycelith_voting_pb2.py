# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mycelith_voting.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15mycelith_voting.proto\x12\x05seigr\"\xd0\x02\n\x0eVotingProposal\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12#\n\x06status\x18\x03 \x01(\x0e\x32\x13.seigr.VotingStatus\x12\"\n\x06layers\x18\x04 \x03(\x0b\x32\x12.seigr.VotingLayer\x12\x14\n\x0ctotal_layers\x18\x05 \x01(\r\x12%\n\x07outcome\x18\x06 \x01(\x0e\x32\x14.seigr.VotingOutcome\x12%\n\x06\x63onfig\x18\x07 \x01(\x0b\x32\x15.seigr.ProposalConfig\x12\x12\n\ncreated_by\x18\x08 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\t \x01(\t\x12\x19\n\x11\x63losing_timestamp\x18\n \x01(\t\x12\x1d\n\x15outcome_justification\x18\x0b \x01(\t\"\xfb\x01\n\x0eProposalConfig\x12\x1d\n\x15\x62\x61se_influence_weight\x18\x01 \x01(\x01\x12\x1c\n\x14influence_multiplier\x18\x02 \x01(\x01\x12\x1a\n\x12\x63onsistency_factor\x18\x03 \x01(\x01\x12\x1a\n\x12min_layers_to_pass\x18\x04 \x01(\r\x12\x1e\n\x16required_participation\x18\x05 \x01(\r\x12\x1b\n\x13\x61\x64\x61ptive_thresholds\x18\x06 \x01(\x08\x12\x1c\n\x14participation_factor\x18\x07 \x01(\x01\x12\x19\n\x11\x65ngagement_factor\x18\x08 \x01(\x01\"\xb7\x01\n\x0bVotingLayer\x12\x14\n\x0clayer_number\x18\x01 \x01(\r\x12\"\n\x06status\x18\x02 \x01(\x0e\x32\x12.seigr.LayerStatus\x12\x1a\n\x05votes\x18\x03 \x03(\x0b\x32\x0b.seigr.Vote\x12\x1d\n\x15layer_influence_total\x18\x04 \x01(\x01\x12\x1a\n\x12total_participants\x18\x05 \x01(\r\x12\x17\n\x0fparticipant_ids\x18\x06 \x03(\t\"\x9a\x01\n\x04Vote\x12\x10\n\x08voter_id\x18\x01 \x01(\t\x12!\n\x06\x63hoice\x18\x02 \x01(\x0e\x32\x11.seigr.VoteChoice\x12\x18\n\x10influence_weight\x18\x03 \x01(\x01\x12\x19\n\x11\x63onsistency_bonus\x18\x04 \x01(\x01\x12\x15\n\ris_consistent\x18\x05 \x01(\x08\x12\x11\n\ttimestamp\x18\x06 \x01(\t\"S\n\x15SubmitProposalRequest\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12%\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x15.seigr.ProposalConfig\"O\n\x16SubmitProposalResponse\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x0f\n\x07message\x18\x03 \x01(\t\"q\n\x0f\x43\x61stVoteRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\x12\x14\n\x0clayer_number\x18\x02 \x01(\r\x12\x10\n\x08voter_id\x18\x03 \x01(\t\x12!\n\x06\x63hoice\x18\x04 \x01(\x0e\x32\x11.seigr.VoteChoice\"i\n\x10\x43\x61stVoteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x18\n\x10influence_weight\x18\x02 \x01(\x01\x12\x19\n\x11\x63onsistency_bonus\x18\x03 \x01(\x01\x12\x0f\n\x07message\x18\x04 \x01(\t\"/\n\x18GetProposalResultRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\"~\n\x19GetProposalResultResponse\x12%\n\x07outcome\x18\x01 \x01(\x0e\x32\x14.seigr.VotingOutcome\x12\x0f\n\x07message\x18\x02 \x01(\t\x12)\n\rlayer_results\x18\x03 \x03(\x0b\x32\x12.seigr.LayerResult\"\x98\x01\n\x0bLayerResult\x12\x14\n\x0clayer_number\x18\x01 \x01(\r\x12\x15\n\ryes_influence\x18\x02 \x01(\x01\x12\x14\n\x0cno_influence\x18\x03 \x01(\x01\x12\x19\n\x11\x61\x62stain_influence\x18\x04 \x01(\x01\x12+\n\rlayer_outcome\x18\x05 \x01(\x0e\x32\x14.seigr.VotingOutcome\"0\n\x19GetProposalDetailsRequest\x12\x13\n\x0bproposal_id\x18\x01 \x01(\t\"\x94\x01\n\x1aGetProposalDetailsResponse\x12\'\n\x08proposal\x18\x01 \x01(\x0b\x32\x15.seigr.VotingProposal\x12\"\n\x06layers\x18\x02 \x03(\x0b\x32\x12.seigr.VotingLayer\x12)\n\naudit_logs\x18\x03 \x03(\x0b\x32\x15.seigr.VotingAuditLog\"f\n\x0eVotingAuditLog\x12\x0e\n\x06log_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x10\n\x08\x61\x63tor_id\x18\x03 \x01(\t\x12\x11\n\ttimestamp\x18\x04 \x01(\t\x12\x0f\n\x07\x64\x65tails\x18\x05 \x01(\t*=\n\x0bLayerStatus\x12\x15\n\x11LAYER_STATUS_OPEN\x10\x00\x12\x17\n\x13LAYER_STATUS_CLOSED\x10\x01*N\n\nVoteChoice\x12\x13\n\x0fVOTE_CHOICE_YES\x10\x00\x12\x12\n\x0eVOTE_CHOICE_NO\x10\x01\x12\x17\n\x13VOTE_CHOICE_ABSTAIN\x10\x02*z\n\x0cVotingStatus\x12\x19\n\x15VOTING_STATUS_PENDING\x10\x00\x12\x18\n\x14VOTING_STATUS_ACTIVE\x10\x01\x12\x1b\n\x17VOTING_STATUS_COMPLETED\x10\x02\x12\x18\n\x14VOTING_STATUS_FAILED\x10\x03*\xa6\x01\n\rVotingOutcome\x12\x1c\n\x18VOTING_OUTCOME_UNDECIDED\x10\x00\x12\x1b\n\x17VOTING_OUTCOME_APPROVED\x10\x01\x12\x1b\n\x17VOTING_OUTCOME_REJECTED\x10\x02\x12\x1c\n\x18VOTING_OUTCOME_ABSTAINED\x10\x03\x12\x1f\n\x1bVOTING_OUTCOME_INCONCLUSIVE\x10\x04\x32\xd6\x02\n\x15MycelithVotingService\x12M\n\x0eSubmitProposal\x12\x1c.seigr.SubmitProposalRequest\x1a\x1d.seigr.SubmitProposalResponse\x12;\n\x08\x43\x61stVote\x12\x16.seigr.CastVoteRequest\x1a\x17.seigr.CastVoteResponse\x12V\n\x11GetProposalResult\x12\x1f.seigr.GetProposalResultRequest\x1a .seigr.GetProposalResultResponse\x12Y\n\x12GetProposalDetails\x12 .seigr.GetProposalDetailsRequest\x1a!.seigr.GetProposalDetailsResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mycelith_voting_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LAYERSTATUS._serialized_start=1993
  _LAYERSTATUS._serialized_end=2054
  _VOTECHOICE._serialized_start=2056
  _VOTECHOICE._serialized_end=2134
  _VOTINGSTATUS._serialized_start=2136
  _VOTINGSTATUS._serialized_end=2258
  _VOTINGOUTCOME._serialized_start=2261
  _VOTINGOUTCOME._serialized_end=2427
  _VOTINGPROPOSAL._serialized_start=33
  _VOTINGPROPOSAL._serialized_end=369
  _PROPOSALCONFIG._serialized_start=372
  _PROPOSALCONFIG._serialized_end=623
  _VOTINGLAYER._serialized_start=626
  _VOTINGLAYER._serialized_end=809
  _VOTE._serialized_start=812
  _VOTE._serialized_end=966
  _SUBMITPROPOSALREQUEST._serialized_start=968
  _SUBMITPROPOSALREQUEST._serialized_end=1051
  _SUBMITPROPOSALRESPONSE._serialized_start=1053
  _SUBMITPROPOSALRESPONSE._serialized_end=1132
  _CASTVOTEREQUEST._serialized_start=1134
  _CASTVOTEREQUEST._serialized_end=1247
  _CASTVOTERESPONSE._serialized_start=1249
  _CASTVOTERESPONSE._serialized_end=1354
  _GETPROPOSALRESULTREQUEST._serialized_start=1356
  _GETPROPOSALRESULTREQUEST._serialized_end=1403
  _GETPROPOSALRESULTRESPONSE._serialized_start=1405
  _GETPROPOSALRESULTRESPONSE._serialized_end=1531
  _LAYERRESULT._serialized_start=1534
  _LAYERRESULT._serialized_end=1686
  _GETPROPOSALDETAILSREQUEST._serialized_start=1688
  _GETPROPOSALDETAILSREQUEST._serialized_end=1736
  _GETPROPOSALDETAILSRESPONSE._serialized_start=1739
  _GETPROPOSALDETAILSRESPONSE._serialized_end=1887
  _VOTINGAUDITLOG._serialized_start=1889
  _VOTINGAUDITLOG._serialized_end=1991
  _MYCELITHVOTINGSERVICE._serialized_start=2430
  _MYCELITHVOTINGSERVICE._serialized_end=2772
# @@protoc_insertion_point(module_scope)