# SQLUser.PA_AdmPackage

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACK_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| PACK_Childsub | double |  |  | NO | Childsub |
| PACK_Comments | varchar |  |  | SI | Comments |
| PACK_PackageGroup_DR | bigint |  | FK | SI | Package Group |
| PACK_PackageSubGroup_DR | bigint |  | FK | SI | Package SubGroup |
| PACK_PersonPackage_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| PACK_Rank | varchar |  |  | SI | Rank |
| PACK_RowId | varchar |  |  | NO | - |
| PACK_Status_DR | bigint |  | FK | SI | Package Status |
| PACK_UpdateDate | date |  |  | SI | UpdateDate |
| PACK_UpdateTime | time |  |  | SI | UpdateTime |
| PACK_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PACK_UpdateUser_DR | bigint |  | FK | SI | Des REf UpdateUser |
| Q01 | - |  |  | SI | Invasive procedure to be performed |
| Q02 | - |  |  | SI | History and physical exam completed (If the patien... |
| Q03 | - |  |  | SI | Informed consent obtained |
| Q04 | - |  |  | SI | Correct patient identity |
| Q05 | - |  |  | SI | Correct site marked |
| Q06 | - |  |  | SI | Correct side marked |
| Q07 | - |  |  | SI | Site |
| Q08 | - |  |  | SI | Correct site verified |
| Q09 | - |  |  | SI | Correct side verified |
| Q10 | - |  |  | SI | Correct equipment available |
| Q11 | - |  |  | SI | Required resources available |
| Q12 | - |  |  | SI | Ready to setup procedure |
| Q13 | - |  |  | SI | Ready to proceed with procedure |
| Q14 | - |  |  | SI | Physician performing procedure |
| Q15 | - |  |  | SI | Physician performing procedure signature |
| Q15UDt | - |  |  | SI | Physician performing procedure signature Last Upda... |
| Q15UTm | - |  |  | SI | Physician performing procedure signature Last Upda... |
| Q16 | - |  |  | SI | Procedure nurse name |
| Q17 | - |  |  | SI | Procedure nurse signature |
| Q17UDt | - |  |  | SI | Procedure nurse signature Last Updated Date |
| Q17UTm | - |  |  | SI | Procedure nurse signature Last Updated Time |
| Q18 | - |  |  | SI | Technician name |
| Q19 | - |  |  | SI | Technician signature |
| Q19UDt | - |  |  | SI | Technician signature Last Updated Date |
| Q19UTm | - |  |  | SI | Technician signature Last Updated Time |
| Q20 | - |  |  | SI | Other |
| Q21 | - |  |  | SI | Other signature |
| Q21UDt | - |  |  | SI | Other signature Last Updated Date |
| Q21UTm | - |  |  | SI | Other signature Last Updated Time |
| Q22 | - |  |  | SI | Other |
| Q23 | - |  |  | SI | Other signature |
| Q23UDt | - |  |  | SI | Other signature Last Updated Date |
| Q23UTm | - |  |  | SI | Other signature Last Updated Time |
| Q24 | - |  |  | SI | Name of procedure, completion of sponge, sharp, an... |
| Q25 | - |  |  | SI | Specimen identified and labeled |
| Q26 | - |  |  | SI | Any equipment problems to be addressed |
| Q27 | - |  |  | SI | Implants and special equipment used were checked |
| Q28 | - |  |  | SI | Safety belt detached after trolley fixed and secur... |
| Q29 | - |  |  | SI | Guide-wire removed |
| Q30 | - |  |  | SI | Date |
| Q31 | - |  |  | SI | Time |
| Q32 | - |  |  | SI | Sign-in |
| Q33 | - |  |  | SI | Sign-in time |
| Q34 | - |  |  | SI | Confirmed patient identity |
| Q35 | - |  |  | SI | Relevant documents, images and studies are availab... |
| Q36 | - |  |  | SI | Timeout |
| Q37 | - |  |  | SI | Timeout time |
| Q38 | - |  |  | SI | Sign-out |
| Q39 | - |  |  | SI | Sign-out time |
| Q40 | - |  |  | SI | Procedure completed as planned? |
| Q41 | - |  |  | SI | Name of procedure that was recorded has been confi... |
| Q42 | - |  |  | SI | Completion of sponge, sharp and instrument counts ... |
| Q43 | - |  |  | SI | Sharps removed from the tray |
| Q44 | - |  |  | SI | Procedure comments |
| Q45 | - |  |  | SI | Procedure start date |
| Q46 | - |  |  | SI | Procedure start time |
| Q47 | - |  |  | SI | Procedure finish date |
| Q48 | - |  |  | SI | Procedure finish time |
| Q49 | - |  |  | SI | Introduction of team members |
| Q50 | - |  |  | SI | Essential lab results available |
| Q51 | - |  |  | SI | Antibiotic prophylaxis given |
| Q52 | - |  |  | SI | Body Site |
| Q53 | - |  |  | SI | Care provider 1 name |
| Q54 | - |  |  | SI | Care provider 2 name |
| Q55 | - |  |  | SI | Care provider 1 name |
| Q56 | - |  |  | SI | Care provider 2 name |
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