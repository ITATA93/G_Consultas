# SQLUser.CT_Region

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRG_RowId | bigint | PK |  | NO | - |
| CTRG_Code | varchar |  |  | NO | Region Code |
| CTRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTRG_Country_DR | bigint |  | FK | NO | Des REf Country |
| CTRG_CreatedDate | date |  |  | SI | Created Date |
| CTRG_CreatedTime | time |  |  | SI | Created Time |
| CTRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTRG_Desc | varchar |  |  | NO | Description |
| CTRG_Owner | varchar |  |  | SI | Owner |
| CTRG_RcFlag | varchar |  |  | SI | Archived Flag |
| CTRG_UpdatedDate | date |  |  | SI | Updated Date |
| CTRG_UpdatedTime | time |  |  | SI | Updated Time |
| CTRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Mother informed by |
| Q02 | - |  |  | SI | Partner informed by |
| Q03 | - |  |  | SI | Consultant obstetrician informed |
| Q03ObsDR | - |  |  | SI | Consultant obstetrician informed DR |
| Q04 | - |  |  | SI | Consultant / senior clinician spoken to parents |
| Q04ObsDR | - |  |  | SI | Consultant / senior clinician spoken to parents DR |
| Q05 | - |  |  | SI | Delivery procedure discussed |
| Q05ObsDR | - |  |  | SI | Delivery procedure discussed DR |
| Q06 | - |  |  | SI | Informed consent obtained and signed |
| Q06ObsDR | - |  |  | SI | Informed consent obtained and signed DR |
| Q07 | - |  |  | SI | Post mortem procedure discussed with doctor |
| Q07ObsDR | - |  |  | SI | Post mortem procedure discussed with doctor DR |
| Q08 | - |  |  | SI | Post mortem consent obtained and signed |
| Q08ObsDR | - |  |  | SI | Post mortem consent obtained and signed DR |
| Q09 | - |  |  | SI | Pathology request completed by doctor |
| Q09ObsDR | - |  |  | SI | Pathology request completed by doctor DR |
| Q10 | - |  |  | SI | Religious advisor required |
| Q10ObsDR | - |  |  | SI | Religious advisor required DR |
| Q11 | - |  |  | SI | Religious advisor called |
| Q11ObsDR | - |  |  | SI | Religious advisor called DR |
| Q12 | - |  |  | SI | Religious ceremony held |
| Q12ObsDR | - |  |  | SI | Religious ceremony held DR |
| Q13 | - |  |  | SI | Photographs offered |
| Q13ObsDR | - |  |  | SI | Photographs offered DR |
| Q14 | - |  |  | SI | Photographs awaited |
| Q14ObsDR | - |  |  | SI | Photographs awaited DR |
| Q15 | - |  |  | SI | Photographs given |
| Q15ObsDR | - |  |  | SI | Photographs given DR |
| Q16 | - |  |  | SI | Birth acknowledgement given |
| Q16ObsDR | - |  |  | SI | Birth acknowledgement given DR |
| Q17 | - |  |  | SI | Cot card given |
| Q17ObsDR | - |  |  | SI | Cot card given DR |
| Q18 | - |  |  | SI | Namebands given |
| Q18ObsDR | - |  |  | SI | Namebands given DR |
| Q19 | - |  |  | SI | Lock of hair given |
| Q19ObsDR | - |  |  | SI | Lock of hair given DR |
| Q20 | - |  |  | SI | Foot/Hand prints given |
| Q20ObsDR | - |  |  | SI | Foot/Hand prints given DR |
| Q21 | - |  |  | SI | Certificate of blessings given |
| Q21ObsDR | - |  |  | SI | Certificate of blessings given DR |
| Q22 | - |  |  | SI | Identification form completed |
| Q22ObsDR | - |  |  | SI | Identification form completed DR |
| Q23 | - |  |  | SI | Request to pathology to collect baby |
| Q23ObsDR | - |  |  | SI | Request to pathology to collect baby DR |
| Q24 | - |  |  | SI | Funeral options discussed |
| Q24ObsDR | - |  |  | SI | Funeral options discussed DR |
| Q25 | - |  |  | SI | Information about funeral arranging given |
| Q25ObsDR | - |  |  | SI | Information about funeral arranging given DR |
| Q26 | - |  |  | SI | Parents decision about funeral |
| Q27 | - |  |  | SI | Special requests |
| Q28 | - |  |  | SI | Religious advisor informed of funeral arrangements |
| Q28ObsDR | - |  |  | SI | Religious advisor informed of funeral arrangements... |
| Q29 | - |  |  | SI | Secretary informed of special requests |
| Q29ObsDR | - |  |  | SI | Secretary informed of special requests DR |
| Q30 | - |  |  | SI | Pathology informed of special requests |
| Q30ObsDR | - |  |  | SI | Pathology informed of special requests DR |
| Q31 | - |  |  | SI | Discussion opportunity with midwife |
| Q31ObsDR | - |  |  | SI | Discussion opportunity with midwife DR |
| Q32 | - |  |  | SI | Discussion opportunity with paediatrician |
| Q32ObsDR | - |  |  | SI | Discussion opportunity with paediatrician DR |
| Q33 | - |  |  | SI | Support literature given |
| Q33ObsDR | - |  |  | SI | Support literature given DR |
| Q34 | - |  |  | SI | Future appointments cancelled |
| Q34ObsDR | - |  |  | SI | Future appointments cancelled DR |
| Q35 | - |  |  | SI | Certificate for baby <24weeks completed |
| Q35ObsDR | - |  |  | SI | Certificate for baby <24weeks completed DR |
| Q36 | - |  |  | SI | Completed form handed to secretary |
| Q36ObsDR | - |  |  | SI | Completed form handed to secretary DR |
| Q37 | - |  |  | SI | Visit from midwife requested |
| Q37ObsDR | - |  |  | SI | Visit from midwife requested DR |
| Q38 | - |  |  | SI | 6 week follow-up appointment arranged |
| Q38ObsDR | - |  |  | SI | 6 week follow-up appointment arranged DR |
| Q39 | - |  |  | SI | GP informed |
| Q39ObsDR | - |  |  | SI | GP informed DR |
| Q40 | - |  |  | SI | Paediatrician informed |
| Q40ObsDR | - |  |  | SI | Paediatrician informed DR |
| Q41 | - |  |  | SI | Clotting screen (urgent) |
| Q41ObsDR | - |  |  | SI | Clotting screen (urgent) DR |
| Q42 | - |  |  | SI | Antibody screen |
| Q42ObsDR | - |  |  | SI | Antibody screen DR |
| Q43 | - |  |  | SI | Antiphospholipid antibodies |
| Q43ObsDR | - |  |  | SI | Antiphospholipid antibodies  DR |
| Q44 | - |  |  | SI | Anticardiolipin antibodies |
| Q44ObsDR | - |  |  | SI | Anticardiolipin antibodies DR |
| Q45 | - |  |  | SI | Glycosylated Hb |
| Q45ObsDR | - |  |  | SI | Glycosylated Hb DR |
| Q46 | - |  |  | SI | TORCH / Parvovirus |
| Q46ObsDR | - |  |  | SI | TORCH / Parvovirus DR |
| Q47 | - |  |  | SI | Urine for chlamydia |
| Q47ObsDR | - |  |  | SI | Urine for chlamydia DR |
| Q48 | - |  |  | SI | Blood cultures listeriosis |
| Q48ObsDR | - |  |  | SI | Blood cultures listeriosis DR |
| Q49 | - |  |  | SI | Liver function tests |
| Q49ObsDR | - |  |  | SI | Liver function tests DR |
| Q50 | - |  |  | SI | Prescription to suppress lactation given |
| Q50ObsDR | - |  |  | SI | Prescription to suppress lactation given DR |
| Q51 | - |  |  | SI | Opportunity to see/holdbaby |
| Q51ObsDR | - |  |  | SI | Opportunity to see/holdbaby DR |
| Q52 | - |  |  | SI | Type of post mortem agreed to |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*