# SQLUser.PAC_WLTypeQuestionnaire

**Schema:** SQLUser
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUEST_ParRef | bigint | PK |  | NO | PAC_WaitingListType Parent Reference |
| ChildQ28DR | - |  |  | SI | Child Reference: Spinal Precautions and Management |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of assessment |
| Q04 | - |  |  | SI | Clinical assessment of cervical spine based on NEX... |
| Q05 | - |  |  | SI | Clinical assessment performed by |
| Q06 | - |  |  | SI | CT assessment of cervical spine |
| Q07 | - |  |  | SI | MRI assessment of cervical spine |
| Q08 | - |  |  | SI | Clinical decision on cervical spine |
| Q09 | - |  |  | SI | Clinical decision made by |
| Q10 | - |  |  | SI | Cervical spine assessment notes |
| Q11 | - |  |  | SI | Thoracic Spine |
| Q12 | - |  |  | SI | Clinical assessment of thoracic spine |
| Q13 | - |  |  | SI | Clinical assessment performed by |
| Q14 | - |  |  | SI | Plain film assessment of thoracic spine |
| Q15 | - |  |  | SI | CT assessment of thoracic spine |
| Q16 | - |  |  | SI | MRI assessment of thoracic spine |
| Q17 | - |  |  | SI | Clinical decision on thoracic spine |
| Q18 | - |  |  | SI | Clinical decision made by |
| Q19 | - |  |  | SI | Thoracic spine assessment notes |
| Q20 | - |  |  | SI | Clinical assessment of lumbar spine |
| Q21 | - |  |  | SI | Clinical assessment performed by |
| Q22 | - |  |  | SI | Plain film assessment of lumbar spine |
| Q23 | - |  |  | SI | CT assessment of lumbar spine |
| Q24 | - |  |  | SI | MRI assessment of lumbar spine |
| Q25 | - |  |  | SI | Clinical decision on lumbar spine |
| Q26 | - |  |  | SI | Clinical decision made by |
| Q27 | - |  |  | SI | Lumbar spine assessment notes |
| Q29 | - |  |  | SI | Steps for spinal clearance |
| Q30 | - |  |  | SI | 1. Assess mechanism and neurology |
| Q31 | - |  |  | SI | 2. Apply NEXUS Criteria for Cervical Spinal Cleara... |
| Q32 | - |  |  | SI | 3. Assess radiology films and report |
| Q33 | - |  |  | SI | 4. Apply mobilisation precautions |
| Q34 | - |  |  | SI | 5. Spinal clearance to be signed off by a senior c... |
| Q35 | - |  |  | SI | Clinical clearance |
| Q36 | - |  |  | SI | Clinical clearance of spine must be performance by... |
| Q37 | - |  |  | SI | i.e. Emergency Department, Intensive Care Unit, Ne... |
| Q38 | - |  |  | SI | Spinal clearance of ICU patients can only be appro... |
| Q39 | - |  |  | SI | Radiology |
| Q40 | - |  |  | SI | All spinal scan films must be verified by neurosur... |
| Q41 | - |  |  | SI | All spinal radiology reports must be verified by c... |
| Q42 | - |  |  | SI | NEXUS Criteria for Cervical Spinal Clearance |
| Q43 | - |  |  | SI | If patients have any of the following 5 criteria p... |
| Q44 | - |  |  | SI | 1. Altered neurologic function/ level of conscious... |
| Q45 | - |  |  | SI | Altered neurologic function is present if any of t... |
| Q46 | - |  |  | SI | a) Glasgow Coma Score 14 or less |
| Q47 | - |  |  | SI | b) Disorientation to person, place, time, or event... |
| Q48 | - |  |  | SI | c) Inability to remember 3 objects at 5 minutes |
| Q49 | - |  |  | SI | d) Delayed or inappropriate response to external s... |
| Q50 | - |  |  | SI | e) Any focal deficit on motor or sensory examinati... |
| Q51 | - |  |  | SI | Patients with none of these individual findings sh... |
| Q52 | - |  |  | SI | 2. Intoxication |
| Q53 | - |  |  | SI | Patients should be considered intoxicated if they ... |
| Q54 | - |  |  | SI | a) A recent history ( can be provided from an obse... |
| Q55 | - |  |  | SI | b) Evidence of intoxication on physical examinatio... |
| Q56 | - |  |  | SI | or other cerebellar findings or any behaviours con... |
| Q57 | - |  |  | SI | Patients may also be considered to be intoxicated ... |
| Q58 | - |  |  | SI | including a blood alcohol level greater than .08mg... |
| Q59 | - |  |  | SI | 3. Posterior midline tenderness |
| Q60 | - |  |  | SI | Midline posterior bony cervical spine tenderness i... |
| Q61 | - |  |  | SI | or if the patient evinces pain with direct palpati... |
| Q62 | - |  |  | SI | 4. Focal neurological deficit |
| Q63 | - |  |  | SI | A focal neurological deficit is any focal neurolog... |
| Q64 | - |  |  | SI | 5. Painful Distracting injuries |
| Q65 | - |  |  | SI | No precise definition of painful distracting injur... |
| Q66 | - |  |  | SI | Therefore this category includes any condition tho... |
| Q67 | - |  |  | SI | Such injuries might include but are not limited to... |
| Q68 | - |  |  | SI | - A long bone fracture |
| Q69 | - |  |  | SI | - A visceral injury requiring surgical consultatio... |
| Q70 | - |  |  | SI | - A large laceration, degloving injury, or crush i... |
| Q71 | - |  |  | SI | - Any other injury producing acute functional impa... |
| Q72 | - |  |  | SI | Physicians may also classify any injury as distrac... |
| Q73 | - |  |  | SI | Dummy 1 |
| Q74 | - |  |  | SI | Dummy 2 |
| Q75 | - |  |  | SI | Dummy 3 |
| Q76 | - |  |  | SI | Dummy 4 |
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
| QUEST_Childsub | double |  |  | NO | Childsub |
| QUEST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUEST_CreatedDate | date |  |  | SI | Created Date |
| QUEST_CreatedTime | time |  |  | SI | Created Time |
| QUEST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUEST_RowId | varchar |  |  | NO | - |
| QUEST_UpdatedDate | date |  |  | SI | Updated Date |
| QUEST_UpdatedTime | time |  |  | SI | Updated Time |
| QUEST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QUEST_UserDefWindow_DR | bigint |  | FK | SI | Des Ref SSUserDefWindow |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*