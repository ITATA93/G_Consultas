# SQLUser.NR_Rostering

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NR_RowId | bigint | PK |  | NO | - |
| NR_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| NR_Date | date |  |  | SI | Date |
| NR_ReqNS | double |  |  | SI | Req NS |
| NR_ReqPAS | double |  |  | SI | ReqPAS |
| NR_ReqTech | double |  |  | SI | Required Technician |
| NR_RosNS | double |  |  | SI | RosNS |
| NR_RosPAS | double |  |  | SI | Ros PAS |
| NR_RosTech | double |  |  | SI | Rostered Technician |
| NR_Shift_DR | bigint |  | FK | SI | Des Ref Shift |
| Q01 | - |  |  | SI | Colour |
| Q02 | - |  |  | SI | Breathing |
| Q03 | - |  |  | SI | Behaviour |
| Q04 | - |  |  | SI | Activity |
| Q05 | - |  |  | SI | Posture |
| Q06 | - |  |  | SI | Face |
| Q07 | - |  |  | SI | Nose |
| Q08 | - |  |  | SI | Mouth |
| Q09 | - |  |  | SI | Ears |
| Q10 | - |  |  | SI | Neck |
| Q11 | - |  |  | SI | Head symmetry |
| Q12 | - |  |  | SI | Head circumference |
| Q12ObsDR | - |  |  | SI | Head circumference DR |
| Q12a | - |  |  | SI | Head circumference |
| Q12aObsDR | - |  |  | SI | Head circumference DR |
| Q13 | - |  |  | SI | Opacities |
| Q14 | - |  |  | SI | Red reflex |
| Q15 | - |  |  | SI | Position |
| Q16 | - |  |  | SI | Heart Rate |
| Q16ObsDR | - |  |  | SI | Heart Rate DR |
| Q17 | - |  |  | SI | Rhythm and sounds |
| Q18 | - |  |  | SI | Murmurs |
| Q19 | - |  |  | SI | Femoral pulse volume |
| Q20 | - |  |  | SI | Shape |
| Q21 | - |  |  | SI | Organomegaly |
| Q22 | - |  |  | SI | Cord |
| Q23 | - |  |  | SI | Effort |
| Q24 | - |  |  | SI | Sounds |
| Q25 | - |  |  | SI | Respiratory rate |
| Q25ObsDR | - |  |  | SI | Respiratory rate DR |
| Q26 | - |  |  | SI | Completeness |
| Q27 | - |  |  | SI | Patency |
| Q28 | - |  |  | SI | Undescended testes |
| Q29 | - |  |  | SI | Bony structure |
| Q30 | - |  |  | SI | Skin integrity |
| Q31 | - |  |  | SI | Texture |
| Q32 | - |  |  | SI | Birthmarks |
| Q33 | - |  |  | SI | Rashes |
| Q34 | - |  |  | SI | Tone |
| Q35 | - |  |  | SI | Hip symmetry |
| Q36 | - |  |  | SI | Skin folds |
| Q37 | - |  |  | SI | Neck |
| Q38 | - |  |  | SI | Clavicles |
| Q39 | - |  |  | SI | Limbs |
| Q40 | - |  |  | SI | Hands |
| Q41 | - |  |  | SI | Feet |
| Q42 | - |  |  | SI | Digits |
| Q43 | - |  |  | SI | Weight |
| Q43ObsDR | - |  |  | SI | Weight DR |
| Q44 | - |  |  | SI | Additional Infomation (Head) |
| Q45 | - |  |  | SI | Additional information (Eyes) |
| Q46 | - |  |  | SI | Additional information (Proportions and Symmetry) |
| Q47 | - |  |  | SI | Additional information (Heart) |
| Q48 | - |  |  | SI | Additional information (Lungs) |
| Q49 | - |  |  | SI | Additional information (Abdomen) |
| Q50 | - |  |  | SI | Additional Information (Genitalia and Anus) |
| Q51 | - |  |  | SI | Additional information (Spine) |
| Q52 | - |  |  | SI | Additional information (Skin) |
| Q53 | - |  |  | SI | Additional information (CNS) |
| Q54 | - |  |  | SI | Additional information (Hips) |
| Q55 | - |  |  | SI | Birth weight |
| Q56 | - |  |  | SI | Additional Information (Birth weight) |
| Q57EYES | - |  |  | SI | Outcome |
| Q57HEART | - |  |  | SI | Outcome |
| Q57OTHER | - |  |  | SI | Any other outcomes |
| Q57TESTES | - |  |  | SI | Outcome |
| Q62 | - |  |  | SI | Galeazzi sign |
| Q63 | - |  |  | SI | Barlows test |
| Q63C | - |  |  | SI | Details |
| Q66 | - |  |  | SI | Fontanelles |
| Q67 | - |  |  | SI | Reflex Grasp |
| Q67HIPS | - |  |  | SI | Outcome |
| Q68 | - |  |  | SI | Moro |
| Q69 | - |  |  | SI | Sucking |
| Q70 | - |  |  | SI | Ortolani test |
| Q71 | - |  |  | SI | Are there any concerns with the following? |
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