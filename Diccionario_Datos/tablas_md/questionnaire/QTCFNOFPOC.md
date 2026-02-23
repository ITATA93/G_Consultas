# questionnaire.QTCFNOFPOC

> Fractured Neck of Femur Post-Operative Care

**Schema:** questionnaire
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fractured Neck of Femur Post-Operative Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Post-op day |
| Q04 | varchar |  |  | SI | Alert and oriented |
| Q05 | varchar |  |  | SI | Variance |
| Q06 | varchar |  |  | SI | Patient monitored and assessed for delirium |
| Q07 | varchar |  |  | SI | Variance |
| Q08 | varchar |  |  | SI | Observations are within acceptable limits and stab... |
| Q09 | varchar |  |  | SI | Variance |
| Q10 | varchar |  |  | SI | Encourage chest physiotherapy as clinically indica... |
| Q11 | varchar |  |  | SI | Variance |
| Q12 | varchar |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q13 | varchar |  |  | SI | Variance |
| Q14 | varchar |  |  | SI | Patient's regular medication prescribed and admini... |
| Q15 | varchar |  |  | SI | Variance |
| Q16 | varchar |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q17 | varchar |  |  | SI | Variance |
| Q18 | varchar |  |  | SI | Patient provided education on using patient-contro... |
| Q19 | varchar |  |  | SI | Variance |
| Q20 | varchar |  |  | SI | IV fluid therapy administered as ordered |
| Q21 | varchar |  |  | SI | Variance |
| Q22 | varchar |  |  | SI | Patient is receiving appropriate venous thrombus p... |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | Patient provided education and demonstrated how to... |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | Patient supervised in the self administration of e... |
| Q27 | varchar |  |  | SI | Variance |
| Q28 | varchar |  |  | SI | All ordered blood tests and investigation taken an... |
| Q29 | varchar |  |  | SI | Variance |
| Q30 | varchar |  |  | SI | All ordered investigations / tests taken and resul... |
| Q31 | varchar |  |  | SI | Variance |
| Q32 | varchar |  |  | SI | Patient is tolerating oral fluids and diet |
| Q33 | varchar |  |  | SI | Variance |
| Q34 | varchar |  |  | SI | Strict fluid balance chart maintained |
| Q35 | varchar |  |  | SI | Variance |
| Q36 | varchar |  |  | SI | Fluid balance chart maintained as required |
| Q37 | varchar |  |  | SI | Variance |
| Q38 | varchar |  |  | SI | Urine output > 30 mLs per hour  |
| Q39 | varchar |  |  | SI | Variance |
| Q40 | varchar |  |  | SI | All bowel motions documented |
| Q41 | varchar |  |  | SI | Variance |
| Q42 | varchar |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q43 | varchar |  |  | SI | Variance |
| Q44 | varchar |  |  | SI | Drain removed as ordered with no complications |
| Q45 | varchar |  |  | SI | Variance |
| Q46 | varchar |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q47 | varchar |  |  | SI | Variance |
| Q48 | varchar |  |  | SI | Patient skin integrity assessed and free from pres... |
| Q49 | varchar |  |  | SI | Variance |
| Q50 | varchar |  |  | SI | Patient has received regular pressure area care wi... |
| Q51 | varchar |  |  | SI | Variance |
| Q52 | varchar |  |  | SI | Personal hygiene attended |
| Q53 | varchar |  |  | SI | Variance |
| Q54 | varchar |  |  | SI | Patient received mouth care as clinically indicate... |
| Q55 | varchar |  |  | SI | Variance |
| Q56 | varchar |  |  | SI | Patient has stood / sat out of bed if appropriate |
| Q57 | varchar |  |  | SI | Variance |
| Q58 | varchar |  |  | SI | Patient reviewed by the physiotherapist and sat ou... |
| Q59 | varchar |  |  | SI | Variance |
| Q60 | varchar |  |  | SI | Patient mobilised with assistance from physiothera... |
| Q61 | varchar |  |  | SI | Variance |
| Q62 | varchar |  |  | SI | All interventions explained to patient / family |
| Q63 | varchar |  |  | SI | Variance |
| Q64 | varchar |  |  | SI | Educate patients regarding signs and symptoms of w... |
| Q65 | varchar |  |  | SI | Variance |
| Q66 | varchar |  |  | SI | Patient provided orientation to ward if required |
| Q67 | varchar |  |  | SI | Variance |
| Q68 | varchar |  |  | SI | Patient safety considered, bedside rails, patient ... |
| Q69 | varchar |  |  | SI | Variance |
| Q70 | varchar |  |  | SI | Patient reviewed by occupational therapist |
| Q71 | varchar |  |  | SI | Variance |
| Q72 | varchar |  |  | SI | Patient reviewed by physiotherapist daily |
| Q73 | varchar |  |  | SI | Variance |
| Q74 | varchar |  |  | SI | Patient reviewed by complex care coordinator |
| Q75 | varchar |  |  | SI | Variance |
| Q76 | varchar |  |  | SI | Referrals to allied health services as required |
| Q77 | varchar |  |  | SI | Variance |
| Q78 | varchar |  |  | SI | Continue discharge planning |
| Q79 | varchar |  |  | SI | Variance |
| Q80 | varchar |  |  | SI | Discharge planning includes: |
| Q81 | varchar |  |  | SI | • Outpatient appointment booked |
| Q82 | varchar |  |  | SI | • Plan for suture removal if required |
| Q83 | varchar |  |  | SI | • Enoxaparin information pack provided to patient |
| Q84 | varchar |  |  | SI | • Community referral for enoxaparin administration... |
| Q85 | varchar |  |  | SI | • Equipment is ready for discharge |
| Q86 | varchar |  |  | SI | • Discharge medications ordered |
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