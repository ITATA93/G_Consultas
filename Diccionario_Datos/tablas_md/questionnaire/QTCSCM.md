# questionnaire.QTCSCM

> Spinal Clearance and Management

**Schema:** questionnaire
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Spinal Clearance and Management

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Type of assessment |
| Q04 | varchar |  |  | SI | Clinical assessment of cervical spine based on NEX... |
| Q05 | varchar |  |  | SI | Clinical assessment performed by |
| Q06 | varchar |  |  | SI | CT assessment of cervical spine |
| Q07 | varchar |  |  | SI | MRI assessment of cervical spine |
| Q08 | varchar |  |  | SI | Clinical decision on cervical spine |
| Q09 | varchar |  |  | SI | Clinical decision made by |
| Q10 | varchar |  |  | SI | Cervical spine assessment notes |
| Q11 | varchar |  |  | SI | Thoracic Spine |
| Q12 | varchar |  |  | SI | Clinical assessment of thoracic spine |
| Q13 | varchar |  |  | SI | Clinical assessment performed by |
| Q14 | varchar |  |  | SI | Plain film assessment of thoracic spine |
| Q15 | varchar |  |  | SI | CT assessment of thoracic spine |
| Q16 | varchar |  |  | SI | MRI assessment of thoracic spine |
| Q17 | varchar |  |  | SI | Clinical decision on thoracic spine  |
| Q18 | varchar |  |  | SI | Clinical decision made by |
| Q19 | varchar |  |  | SI | Thoracic spine assessment notes |
| Q20 | varchar |  |  | SI | Clinical assessment of lumbar spine |
| Q21 | varchar |  |  | SI | Clinical assessment performed by |
| Q22 | varchar |  |  | SI | Plain film assessment of lumbar spine |
| Q23 | varchar |  |  | SI | CT assessment of lumbar spine |
| Q24 | varchar |  |  | SI | MRI assessment of lumbar spine |
| Q25 | varchar |  |  | SI | Clinical decision on lumbar spine  |
| Q26 | varchar |  |  | SI | Clinical decision made by |
| Q27 | varchar |  |  | SI | Lumbar spine assessment notes |
| Q29 | varchar |  |  | SI | Steps for spinal clearance |
| Q30 | varchar |  |  | SI | 1. Assess mechanism and neurology |
| Q31 | varchar |  |  | SI | 2. Apply NEXUS Criteria for Cervical Spinal Cleara... |
| Q32 | varchar |  |  | SI | 3. Assess radiology films and report |
| Q33 | varchar |  |  | SI | 4. Apply mobilisation precautions |
| Q34 | varchar |  |  | SI | 5. Spinal clearance to be signed off by a senior c... |
| Q35 | varchar |  |  | SI | Clinical clearance |
| Q36 | varchar |  |  | SI | Clinical clearance of spine must be performance by... |
| Q37 | varchar |  |  | SI | i.e. Emergency Department, Intensive Care Unit, Ne... |
| Q38 | varchar |  |  | SI | Spinal clearance of ICU patients can only be appro... |
| Q39 | varchar |  |  | SI | Radiology |
| Q40 | varchar |  |  | SI | All spinal scan films must be verified by neurosur... |
| Q41 | varchar |  |  | SI | All spinal radiology reports must be verified by c... |
| Q42 | varchar |  |  | SI | NEXUS Criteria for Cervical Spinal Clearance |
| Q43 | varchar |  |  | SI | If patients have any of the following 5 criteria p... |
| Q44 | varchar |  |  | SI | 1. Altered neurologic function/ level of conscious... |
| Q45 | varchar |  |  | SI | Altered neurologic function is present if any of t... |
| Q46 | varchar |  |  | SI | a) Glasgow Coma Score 14 or less; |
| Q47 | varchar |  |  | SI | b) Disorientation to person, place, time, or event... |
| Q48 | varchar |  |  | SI | c) Inability to remember 3 objects at 5 minutes; |
| Q49 | varchar |  |  | SI | d) Delayed or inappropriate response to external s... |
| Q50 | varchar |  |  | SI | e) Any focal deficit on motor or sensory examinati... |
| Q51 | varchar |  |  | SI | Patients with none of these individual findings sh... |
| Q52 | varchar |  |  | SI | 2. Intoxication |
| Q53 | varchar |  |  | SI | Patients should be considered intoxicated if they ... |
| Q54 | varchar |  |  | SI | a) A recent history ( can be provided from an obse... |
| Q55 | varchar |  |  | SI | b) Evidence of intoxication on physical examinatio... |
| Q56 | varchar |  |  | SI | or other cerebellar findings or any behaviours con... |
| Q57 | varchar |  |  | SI | Patients may also be considered to be intoxicated ... |
| Q58 | varchar |  |  | SI | including a blood alcohol level greater than .08mg... |
| Q59 | varchar |  |  | SI | 3. Posterior midline tenderness |
| Q60 | varchar |  |  | SI | Midline posterior bony cervical spine tenderness i... |
| Q61 | varchar |  |  | SI | or if the patient evinces pain with direct palpati... |
| Q62 | varchar |  |  | SI | 4. Focal neurological deficit |
| Q63 | varchar |  |  | SI | A focal neurological deficit is any focal neurolog... |
| Q64 | varchar |  |  | SI | 5. Painful Distracting injuries |
| Q65 | varchar |  |  | SI | No precise definition of painful distracting injur... |
| Q66 | varchar |  |  | SI | Therefore this category includes any condition tho... |
| Q67 | varchar |  |  | SI | Such injuries might include but are not limited to... |
| Q68 | varchar |  |  | SI | - A long bone fracture |
| Q69 | varchar |  |  | SI | - A visceral injury requiring surgical consultatio... |
| Q70 | varchar |  |  | SI | - A large laceration, degloving injury, or crush i... |
| Q71 | varchar |  |  | SI | - Any other injury producing acute functional impa... |
| Q72 | varchar |  |  | SI | Physicians may also classify any injury as distrac... |
| Q73 | varchar |  |  | SI | Dummy 1 |
| Q74 | varchar |  |  | SI | Dummy 2 |
| Q75 | varchar |  |  | SI | Dummy 3 |
| Q76 | varchar |  |  | SI | Dummy 4 |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*