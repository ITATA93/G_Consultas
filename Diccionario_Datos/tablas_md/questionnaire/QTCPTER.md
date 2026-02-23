# questionnaire.QTCPTER

> Post Transplant Education Record

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Post Transplant Education Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Post Transplant Routine |
| Q04 | varchar |  |  | SI | Location of clinic and contact details |
| Q05 | varchar |  |  | SI | Reporting symptoms and to whom |
| Q06 | varchar |  |  | SI | Protocol biopsy |
| Q07 | varchar |  |  | SI | Frequency of bloods |
| Q08 | varchar |  |  | SI | Glucose tolerance test |
| Q09 | varchar |  |  | SI | Medication Management |
| Q10 | varchar |  |  | SI | Importance of taking immunosuppression regularly |
| Q11 | varchar |  |  | SI | Use of apps and reminders to take medication at re... |
| Q12 | varchar |  |  | SI | Foods to avoid |
| Q13 | varchar |  |  | SI | Medications |
| Q14 | varchar |  |  | SI | Acute and chronic rejection, possible treatment re... |
| Q15 | varchar |  |  | SI | Managing Infection: Risks |
| Q16 | varchar |  |  | SI | Importance of handwashing |
| Q17 | varchar |  |  | SI | Check temperature if unwell |
| Q18 | varchar |  |  | SI | Avoid people with contagious infections |
| Q19 | varchar |  |  | SI | When to contact Transplant team |
| Q20 | varchar |  |  | SI | Flu vaccination recommended every year |
| Q21 | varchar |  |  | SI | Children and pets |
| Q22 | varchar |  |  | SI | Cancer Prevention |
| Q23 | varchar |  |  | SI | Importance of seeing a dermatologist regularly |
| Q24 | varchar |  |  | SI | Protect skin from UV rays / sun |
| Q25 | varchar |  |  | SI | Regular mammogram / cervical screening |
| Q26 | varchar |  |  | SI | Regular prostate screening |
| Q27 | varchar |  |  | SI | Regular bowel screening and colonoscopy |
| Q28 | varchar |  |  | SI | Abdominal ultrasound to detect intra-abdominal tum... |
| Q29 | varchar |  |  | SI | Nephrologist discusses risks of cancer |
| Q30 | varchar |  |  | SI | Maintaining a Healthy Lifestyle |
| Q31 | varchar |  |  | SI | Regular  GP health checks |
| Q32 | varchar |  |  | SI | Regular dental checks |
| Q33 | varchar |  |  | SI | Preparing for travel  and holidays |
| Q34 | varchar |  |  | SI | Daily fluid intake |
| Q35 | varchar |  |  | SI | Regular exercise |
| Q36 | varchar |  |  | SI | Avoid cigarettes and smoking |
| Q37 | varchar |  |  | SI | Limit alcohol consumption |
| Q38 | varchar |  |  | SI | Healthy diet |
| Q39 | varchar |  |  | SI | Annual tests required |
| Q40 | varchar |  |  | SI | Contraception and pregnancy |
| Q41 | varchar |  |  | SI | Donor Family Contact |
| Q42 | varchar |  |  | SI | Thank you letter to the donor family |
| Q43 | varchar |  |  | SI | Donate life -service of remembrance |
| Q44 | varchar |  |  | SI | Patient Understanding |
| Q45 | varchar |  |  | SI | Patient able to verbalise topics discussed in own ... |
| Q46 | varchar |  |  | SI | Comments on education provided and patient underst... |
| Q47 | varchar |  |  | SI | Medications |
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