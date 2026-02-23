# SQLUser.MR_EncEntryItem

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITEM_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ITEM_Childsub | double |  |  | NO | Childsub |
| ITEM_ClassName | varchar |  |  | SI | ClassName that the ITEMDocItemID refers to |
| ITEM_CopyFromItem_DR | varchar |  | FK | SI | Copied from Original Encounter Entry Item |
| ITEM_CreateDate | date |  |  | SI | - |
| ITEM_CreateTime | time |  |  | SI | - |
| ITEM_Deleted | bit |  |  | SI | Shows if Entry Item has been deleted because it ha... |
| ITEM_DeletedDate | date |  |  | SI | Date Entry Item was deleted |
| ITEM_DeletedTime | time |  |  | SI | Time Entry Item was deleted |
| ITEM_DeletedUser_DR | bigint |  | FK | SI | User who deleted the Entry Item  |
| ITEM_DocItemID | varchar |  |  | SI | this contains the ID of the documentation item (it... |
| ITEM_DocItemParams | varchar |  |  | SI | parameters to uniquely identify the doc item and o... |
| ITEM_DocItemTypeDR | bigint |  | FK | NO | - |
| ITEM_DocItemUpdateDate | date |  |  | SI | last update date of doc item when it was created/a... |
| ITEM_DocItemUpdateTime | time |  |  | SI | last update time of doc item when it was created/a... |
| ITEM_EditURL | varchar |  |  | SI | Edit URL for the Entry Item  |
| ITEM_EncounterAction_DR | bigint |  | FK | SI | Encounter Action reference |
| ITEM_EntryTypeAction_DR | varchar |  | FK | SI | Encounter Entry Type Action |
| ITEM_LastUpdateUser_DR | bigint |  | FK | SI | User who last updated the Entry Item |
| ITEM_LinkSectionDR | varchar |  | FK | SI | Item LinkSectionDR for sorting null ESECT_Sequence |
| ITEM_LockedHeaderDesc | varchar |  |  | SI | LOCKED: Header Description |
| ITEM_LockedItemSequence | integer |  |  | SI | LOCKED: Item Sequence |
| ITEM_LockedSectionDesc | varchar |  |  | SI | LOCKED: Section Description |
| ITEM_Notes | varchar |  |  | SI | notes that can be made for each entry item |
| ITEM_RowId | varchar |  |  | NO | - |
| ITEM_Sequence | varchar |  |  | SI | Item Sequence for sorting null ESECT_Sequence |
| ITEM_Status | integer |  |  | SI | Added or New (see webMREncounter.inc) |
| ITEM_TextRep | varchar |  |  | SI | - |
| ITEM_TextRepDocument_DR | bigint |  | FK | SI | Text Rep Document |
| ITEM_TextRepDocuments | varchar |  |  | SI | A list of Text Rep Document |
| ITEM_TextRepRecent | varchar |  |  | SI | Text representation of the most recent version of ... |
| ITEM_UnsavedData_DR | varchar |  | FK | SI | Encounter Entry Unsaved Data reference |
| ITEM_User_DR | bigint |  | FK | SI | - |
| Q01 | - |  |  | SI | Level of consciousness |
| Q02 | - |  |  | SI | Cyanosis |
| Q03 | - |  |  | SI | Stridor |
| Q04 | - |  |  | SI | Air entry |
| Q05 | - |  |  | SI | Retractions |
| Q06 | - |  |  | SI | 0 to 2: Mild , Occasional barky cough, no stridor ... |
| Q06a | - |  |  | SI | Home treatment: Symptomatic care including antipyr... |
| Q06b | - |  |  | SI | Outpatient treatment: Single dose of oral dexameth... |
| Q07 | - |  |  | SI | 3 to 7: Moderate , Frequent barky cough, stridor a... |
| Q07a | - |  |  | SI | Single dose of oral dexamethasone 0.6 mg/kg (maxim... |
| Q07b | - |  |  | SI | Nebulized epinephrine |
| Q07c | - |  |  | SI | Hospitalization is generally not needed, but may b... |
| Q08 | - |  |  | SI | 8 to 11: Severe , Frequent barky cough, stridor at... |
| Q08a | - |  |  | SI | Single dose of oral / IM / IV dexamethasone 0.6 mg... |
| Q08b | - |  |  | SI | Repeated doses of nebulized epinephrine** may be n... |
| Q08c | - |  |  | SI | Inpatient admission is generally required unless m... |
| Q09 | - |  |  | SI | 12 to 17: Impending respiratory failure , Depresse... |
| Q09a | - |  |  | SI | Single dose of IM/IV dexamethasone 0.6 mg/kg (maxi... |
| Q09b | - |  |  | SI | Repeated doses of nebulized epinephrine** may be n... |
| Q09c | - |  |  | SI | Intensive care unit admission is generally require... |
| Q09d | - |  |  | SI | Consultation with anesthesiologist or ENT surgeon ... |
| Q10 | - |  |  | SI | Management |
| Q23 | - |  |  | SI | Westley croup severity score (Acute laryngotracheo... |
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