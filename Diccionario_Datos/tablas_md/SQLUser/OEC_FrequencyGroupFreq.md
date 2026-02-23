# SQLUser.OEC_FrequencyGroupFreq

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FREQ_ParRef | bigint | PK |  | NO | OEC_FrequencyGroup Parent Reference |
| FREQ_Childsub | double |  |  | NO | Childsub |
| FREQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FREQ_CreatedDate | date |  |  | SI | Created Date |
| FREQ_CreatedTime | time |  |  | SI | Created Time |
| FREQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FREQ_DateFrom | date |  |  | SI | DateFrom |
| FREQ_DateTo | date |  |  | SI | DateTo |
| FREQ_Freq_DR | bigint |  | FK | SI | Des Ref PHCFreq |
| FREQ_RowId | varchar |  |  | NO | - |
| FREQ_UpdatedDate | date |  |  | SI | Updated Date |
| FREQ_UpdatedTime | time |  |  | SI | Updated Time |
| FREQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Diagnosis |
| Q02 | - |  |  | SI | Dilation with |
| Q03 | - |  |  | SI | External |
| Q04 | - |  |  | SI | Other |
| Q05 | - |  |  | SI | Slit lamp |
| Q06 | - |  |  | SI | With Fluorescein / rose bengal |
| Q07 | - |  |  | SI | Lids |
| Q08 | - |  |  | SI | Cornea |
| Q09 | - |  |  | SI | Iris |
| Q10 | - |  |  | SI | Lens |
| Q11 | - |  |  | SI | Conjunctiva |
| Q12 | - |  |  | SI | Gonioscopy |
| Q13 | - |  |  | SI | Specular microscopy |
| Q14 | - |  |  | SI | Endothial cell account needed in |
| Q15 | - |  |  | SI | Cell count: cell/mm2 |
| Q16 | - |  |  | SI | Cell count 2 |
| Q17 | - |  |  | SI | Polymegathism |
| Q18 | - |  |  | SI | Polymegathism 2 |
| Q19 | - |  |  | SI | Polymorphism |
| Q20 | - |  |  | SI | Polymorphism 2 |
| Q21 | - |  |  | SI | Guttata |
| Q22 | - |  |  | SI | Guttata 2 |
| Q23 | - |  |  | SI | Fundus |
| Q24 | - |  |  | SI | Color fundus photo |
| Q25 | - |  |  | SI | DR-7 filed view |
| Q26 | - |  |  | SI | stereo |
| Q27 | - |  |  | SI | Discs |
| Q28 | - |  |  | SI | Auto fluorescence |
| Q29 | - |  |  | SI | Fluorescin angiography |
| Q30 | - |  |  | SI | Trasit phase |
| Q31 | - |  |  | SI | Late photo at |
| Q32 | - |  |  | SI | minutes |
| Q33 | - |  |  | SI | View |
| Q34 | - |  |  | SI | Indocyanine green angiography |
| Q35 | - |  |  | SI | Transit phase |
| Q36 | - |  |  | SI | Notes |
| Q37 | - |  |  | SI | Image Annotation |
| Q38 | - |  |  | SI | Right Eye |
| Q39 | - |  |  | SI | Left eye |
| Q40 | - |  |  | SI | Image |
| Q41 | - |  |  | SI | General |
| Q42 | - |  |  | SI | Date |
| Q43 | - |  |  | SI | Time |
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