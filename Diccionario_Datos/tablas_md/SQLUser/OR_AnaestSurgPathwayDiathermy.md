# SQLUser.OR_AnaestSurgPathwayDiathermy

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIATH_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| DIATH_Childsub | numeric |  |  | NO | Childsub |
| DIATH_DiathMethod_DR | bigint |  | FK | NO |  Des Ref ORCDiathermyMethod |
| DIATH_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Post-op day |
| Q04 | - |  |  | SI | Alert and oriented |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Patient monitored and assessed for delirium |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Encourage chest physiotherapy as clinically indica... |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | Neurovascular observations remain aligned to basel... |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Patient's regular medication prescribed and admini... |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Patient provided education on using patient-contro... |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | IV fluid therapy administered as ordered |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Patient is receiving appropriate venous thrombus p... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Patient provided education and demonstrated how to... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Patient supervised in the self administration of e... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | All ordered blood tests and investigation taken an... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | All ordered investigations / tests taken and resul... |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Patient is tolerating oral fluids and diet |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Strict fluid balance chart maintained |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Fluid balance chart maintained as required |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Urine output > 30 mLs per hour |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | All bowel motions documented |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Regular and PRN aperients prescribed and administe... |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Drain removed as ordered with no complications |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Surgical wound observed for signs of haematoma, oo... |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Patient skin integrity assessed and free from pres... |
| Q49 | - |  |  | SI | Variance |
| Q50 | - |  |  | SI | Patient has received regular pressure area care wi... |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Personal hygiene attended |
| Q53 | - |  |  | SI | Variance |
| Q54 | - |  |  | SI | Patient received mouth care as clinically indicate... |
| Q55 | - |  |  | SI | Variance |
| Q56 | - |  |  | SI | Patient has stood / sat out of bed if appropriate |
| Q57 | - |  |  | SI | Variance |
| Q58 | - |  |  | SI | Patient reviewed by the physiotherapist and sat ou... |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Patient mobilised with assistance from physiothera... |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | All interventions explained to patient / family |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Educate patients regarding signs and symptoms of w... |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Patient provided orientation to ward if required |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Patient safety considered, bedside rails, patient ... |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Patient reviewed by occupational therapist |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | Patient reviewed by physiotherapist daily |
| Q73 | - |  |  | SI | Variance |
| Q74 | - |  |  | SI | Patient reviewed by complex care coordinator |
| Q75 | - |  |  | SI | Variance |
| Q76 | - |  |  | SI | Referrals to allied health services as required |
| Q77 | - |  |  | SI | Variance |
| Q78 | - |  |  | SI | Continue discharge planning |
| Q79 | - |  |  | SI | Variance |
| Q80 | - |  |  | SI | Discharge planning includes: |
| Q81 | - |  |  | SI | • Outpatient appointment booked |
| Q82 | - |  |  | SI | • Plan for suture removal if required |
| Q83 | - |  |  | SI | • Enoxaparin information pack provided to patient |
| Q84 | - |  |  | SI | • Community referral for enoxaparin administration... |
| Q85 | - |  |  | SI | • Equipment is ready for discharge |
| Q86 | - |  |  | SI | • Discharge medications ordered |
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