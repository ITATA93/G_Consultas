# SQLUser.DICOM_WorkList

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Imágenes Diagnósticas**. Radiología y estudios de imagen.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Insertion site |
| Q01ObsDR | - |  |  | SI | Insertion site DR |
| Q02 | - |  |  | SI | Cannula type |
| Q02ObsDR | - |  |  | SI | Cannula type DR |
| Q03 | - |  |  | SI | Cannula gauge |
| Q03ObsDR | - |  |  | SI | Cannula gauge DR |
| Q04 | - |  |  | SI | Insertion attempts |
| Q04ObsDR | - |  |  | SI | Insertion attempts DR |
| Q05 | - |  |  | SI | Dressing |
| Q05ObsDR | - |  |  | SI | Dressing DR |
| Q06 | - |  |  | SI | Site preparation |
| Q06ObsDR | - |  |  | SI | Site preparation DR |
| Q07 | - |  |  | SI | Infection control |
| Q08 | - |  |  | SI | Person who placed IV |
| Q09 | - |  |  | SI | Insertion date |
| Q10 | - |  |  | SI | Insertion time |
| Q11 | - |  |  | SI | Removal reason |
| Q11ObsDR | - |  |  | SI | Removal reason DR |
| Q12 | - |  |  | SI | Removal date |
| Q13 | - |  |  | SI | Removal time |
| Q14 | - |  |  | SI | Safety precautions |
| Q15 | - |  |  | SI | Line type |
| Q16 | - |  |  | SI | Catheter type |
| Q17 | - |  |  | SI | Catheter gauge |
| Q18 | - |  |  | SI | Patient information leaflets given	 |
| Q19 | - |  |  | SI | Indication of IV access	 |
| Q20 | - |  |  | SI | Mark site with an X on image below	 |
| Q21 | - |  |  | SI | Bodymap |
| Q22 | - |  |  | SI | Number of attempts	 |
| Q23 | - |  |  | SI | Aseptic Non Touch Technique (ANTT) adhered to	 |
| Q24 | - |  |  | SI | Reason for deviation	 |
| Q25 | - |  |  | SI | Inserted by ambulance crew	 |
| Q26 | - |  |  | SI | Inserted during clinical emergency / resuscitation... |
| Q27 | - |  |  | SI | Visual Infusion Phlebitis (VIP) score on removal	 |
| Q28 | - |  |  | SI | Notes |
| Q29 | - |  |  | SI | Observation |
| Q30 | - |  |  | SI | No sign of Phlebitis.  Observe PIVC & ensure docum... |
| Q31 | - |  |  | SI | Possible first sign of Phlebitis.  Remove PIVC, re... |
| Q32 | - |  |  | SI | Early Phlebitis: Remove PIVC , resite is necessary... |
| Q33 | - |  |  | SI | Medium Phlebitis: Remove PIVC, resite is necessary... |
| Q34 | - |  |  | SI | Advance Phlebitis:  Remove PIVC, resite if neneces... |
| Q35 | - |  |  | SI | Advance Thrombophlebitis:  Remove PIVC, initiate T... |
| Q36 | - |  |  | SI | Please consider Referral to IV team	 |
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
| WL_AccessionNumber | varchar |  |  | SI | Accession Number |
| WL_Date | date |  |  | SI | Date |
| WL_Modality | varchar |  |  | SI | Modality |
| WL_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| WL_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| WL_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| WL_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*