# SQLUser.PAC_BedStatus

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BSTAT_RowId | bigint | PK |  | NO | - |
| BSTAT_Code | varchar |  |  | NO | Code |
| BSTAT_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| BSTAT_CreatedDate | date |  |  | SI | Created Date |
| BSTAT_CreatedTime | time |  |  | SI | Created Time |
| BSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BSTAT_Desc | varchar |  |  | NO | Description |
| BSTAT_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| BSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| BSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| BSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ICU presenting problem |
| Q01TxtOnly | - |  |  | SI | ICU presenting problem Plain Text Only |
| Q02 | - |  |  | SI | ICU clinical examination |
| Q02TxtOnly | - |  |  | SI | ICU clinical examination Plain Text Only |
| Q03 | - |  |  | SI | ICU active problems |
| Q03TxtOnly | - |  |  | SI | ICU active problems Plain Text Only |
| Q04 | - |  |  | SI | ICU plan |
| Q04TxtOnly | - |  |  | SI | ICU plan Plain Text Only |
| Q05 | - |  |  | SI | ICU admission summary |
| Q05TxtOnly | - |  |  | SI | ICU admission summary Plain Text Only |
| Q06 | - |  |  | SI | ICU discharge plan |
| Q06TxtOnly | - |  |  | SI | ICU discharge plan Plain Text Only |
| Q07 | - |  |  | SI | Date |
| Q08 | - |  |  | SI | Time |
| Q09 | - |  |  | SI | Staff present on round |
| Q10 | - |  |  | SI | ICU presenting complaint |
| Q11 | - |  |  | SI | ICU active issues |
| Q12 | - |  |  | SI | ICU clinical examination |
| Q13 | - |  |  | SI | ICU plan |
| Q14 | - |  |  | SI | ICU admission summary |
| Q15 | - |  |  | SI | ICU discharge plan |
| Q16 | - |  |  | SI | Considerations During ICU Medical Round |
| Q17 | - |  |  | SI | Review invasive lines |
| Q18 | - |  |  | SI | Review for extubation |
| Q19 | - |  |  | SI | Deep Vein Thrombosis (DVT) prophylaxis |
| Q20 | - |  |  | SI | Peptic ulcer prophylaxis |
| Q21 | - |  |  | SI | Review antibiotics |
| Q22 | - |  |  | SI | Ventilator Associated Pneumonia (VAP) antibiotics |
| Q23 | - |  |  | SI | Sedation / Analgesia / CAM-ICU score |
| Q24 | - |  |  | SI | Nutritional planning |
| Q25 | - |  |  | SI | Bowels / Aperients |
| Q26 | - |  |  | SI | C-spine considered |
| Q27 | - |  |  | SI | Dummy 1 |
| Q28 | - |  |  | SI | Dummy 2 |
| Q29 | - |  |  | SI | Considerations for ICU Medical Discharge |
| Q30 | - |  |  | SI | ICU team leader aware |
| Q31 | - |  |  | SI | Ward team handover |
| Q32 | - |  |  | SI | Discharge summary completed |
| Q33 | - |  |  | SI | Plan for invasive devices documented in the discha... |
| Q34 | - |  |  | SI | Medication review completed |
| Q35 | - |  |  | SI | Patient and family informed |
| Q36 | - |  |  | SI | Dummy 3 |
| Q37 | - |  |  | SI | Dummy 4 |
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