# questionnaire.QTCPAR

> Perineal Assessment and Repair

**Schema:** questionnaire
**Columnas:** 187
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perineal Assessment and Repair

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Consent for perineal assessment |
| Q04 | varchar |  |  | SI | Rectal examination before repair |
| Q05 | varchar |  |  | SI | Details |
| Q06 | varchar |  |  | SI | Anterior trauma and tears |
| Q07 | varchar |  |  | SI | Notes |
| Q08 | varchar |  |  | SI | Degree of tear |
| Q09 | varchar |  |  | SI | Third degree description |
| Q10 | varchar |  |  | SI | Episiotomy |
| Q100 | varchar |  |  | SI | Vaginal pack(s) intentionally retained in situ |
| Q101 | varchar |  |  | SI | Tampon(s) intentionally retained in situ |
| Q102 | varchar |  |  | SI | Non - absorbable suture for removal |
| Q103 | varchar |  |  | SI | Final Count |
| Q104 | numeric |  |  | SI | Suture(s) |
| Q105 | numeric |  |  | SI | Ties(s) |
| Q106 | numeric |  |  | SI | Pack(s) |
| Q107 | numeric |  |  | SI | Swab(s) |
| Q108 | numeric |  |  | SI | Suture needle(s) |
| Q109 | numeric |  |  | SI | Syringe needle(s) |
| Q11 | varchar |  |  | SI | Indication for episiotomy |
| Q110 | numeric |  |  | SI | Sponge(s) |
| Q111 | numeric |  |  | SI | Tampon(s) |
| Q112 | varchar |  |  | SI | Final Repair Actions |
| Q113 | varchar |  |  | SI | Count deficit |
| Q114 | varchar |  |  | SI | Action taken |
| Q115 | varchar |  |  | SI | Count performed by |
| Q116 | longvarbinary |  |  | SI | Signature |
| Q116UDt | date |  |  | SI | Signature Last Updated Date |
| Q116UTm | time |  |  | SI | Signature Last Updated Time |
| Q117 | varchar |  |  | SI | Witness to count procedure |
| Q118 | longvarbinary |  |  | SI | Signature |
| Q118UDt | date |  |  | SI | Signature Last Updated Date |
| Q118UTm | time |  |  | SI | Signature Last Updated Time |
| Q119 | varchar |  |  | SI | Post repair analgesia required |
| Q12 | varchar |  |  | SI | Female genital mutilation |
| Q120 | varchar |  |  | SI | Prophylactic antibiotics used |
| Q121 | varchar |  |  | SI | Laxatives required |
| Q122 | varchar |  |  | SI | Follow - up referral(s) required |
| Q123 | varchar |  |  | SI | Information provided to patient |
| Q124 | varchar |  |  | SI | Notes |
| Q125 | varchar |  |  | SI | Care provider 1 |
| Q126 | longvarbinary |  |  | SI | Signature |
| Q126UDt | date |  |  | SI | Signature Last Updated Date |
| Q126UTm | time |  |  | SI | Signature Last Updated Time |
| Q127 | varchar |  |  | SI | Care provider 2 |
| Q128 | longvarbinary |  |  | SI | Signature |
| Q128UDt | date |  |  | SI | Signature Last Updated Date |
| Q128UTm | time |  |  | SI | Signature Last Updated Time |
| Q129 | varchar |  |  | SI | Number of vaginal pack(s) intentionally retained i... |
| Q129ObsDR | varchar |  | FK | SI | Number of vaginal pack(s) intentionally retained i... |
| Q13 | varchar |  |  | SI | Female genital mutilation classification |
| Q130 | varchar |  |  | SI | Number of tampon(s) intentionally retained in situ |
| Q130ObsDR | varchar |  | FK | SI | Number of tampon(s) intentionally retained in situ... |
| Q131 | varchar |  |  | SI | Notes |
| Q132 | varchar |  |  | SI | Notes |
| Q14 | varchar |  |  | SI | Anterior incision performed at birth |
| Q15 | varchar |  |  | SI | Initial Repair Actions |
| Q16 | varchar |  |  | SI | Repair required |
| Q17 | varchar |  |  | SI | Communicated with patient |
| Q18 | varchar |  |  | SI | Consent for repair |
| Q19 | varchar |  |  | SI | Notes |
| Q20 | date |  |  | SI | Repair start date |
| Q21 | time |  |  | SI | Repair start time |
| Q22 | varchar |  |  | SI | Patient position |
| Q23 | varchar |  |  | SI | Initial Count |
| Q24 | numeric |  |  | SI | Suture(s) |
| Q25 | numeric |  |  | SI | Ties(s) |
| Q26 | numeric |  |  | SI | Pack(s) |
| Q27 | numeric |  |  | SI | Swab(s) |
| Q28 | numeric |  |  | SI | Suture needle(s) |
| Q29 | numeric |  |  | SI | Syringe needle(s) |
| Q30 | numeric |  |  | SI | Sponge(s) |
| Q31 | numeric |  |  | SI | Tampon(s) |
| Q32 | varchar |  |  | SI | Count performed by |
| Q33 | longvarbinary |  |  | SI | Signature |
| Q33UDt | date |  |  | SI | Signature Last Updated Date |
| Q33UTm | time |  |  | SI | Signature Last Updated Time |
| Q34 | varchar |  |  | SI | Witness to count procedure |
| Q35 | longvarbinary |  |  | SI | Signature |
| Q35UDt | date |  |  | SI | Signature Last Updated Date |
| Q35UTm | time |  |  | SI | Signature Last Updated Time |
| Q36 | varchar |  |  | SI | Repair Procedure Details |
| Q37 | varchar |  |  | SI | Indwelling catheter inserted |
| Q38 | varchar |  |  | SI | Intermittent catheterisation |
| Q39 | varchar |  |  | SI | Anaesthetic method(s) used for repair |
| Q41 | varchar |  |  | SI | Non - standard equipment / any equipment issues |
| Q42 | varchar |  |  | SI | Repair notes |
| Q43 | varchar |  |  | SI | Diagram |
| Q44 | varchar |  |  | SI | Consult requested during repair |
| Q45 | varchar |  |  | SI | Consult provided by |
| Q46 | varchar |  |  | SI | Rectal examination after repair |
| Q47 | varchar |  |  | SI | Details |
| Q48 | varchar |  |  | SI | Post vaginal examination completed |
| Q49 | varchar |  |  | SI | Volume of blood loss during repair |
| Q49ObsDR | varchar |  | FK | SI | Volume of blood loss during repair DR |
| Q50 | varchar |  |  | SI | mL |
| Q51 | varchar |  |  | SI | Please be aware of the volume of blood loss during... |
| Q52 | varchar |  |  | SI | Calculation method |
| Q53 | date |  |  | SI | Repair finish date |
| Q54 | time |  |  | SI | Repair finish time |
| Q55 | varchar |  |  | SI | Repaired by |
| Q56 | varchar |  |  | SI | Repair supervised |
| Q57 | varchar |  |  | SI | Supervisor |
| Q58 | varchar |  |  | SI | Count Details |
| Q59 | varchar |  |  | SI | Suture(s) |
| Q60 | numeric |  |  | SI | Before procedure |
| Q61 | numeric |  |  | SI | 1st addition |
| Q62 | numeric |  |  | SI | 2nd addition |
| Q63 | numeric |  |  | SI | After procedure |
| Q64 | varchar |  |  | SI | Tie(s) |
| Q65 | numeric |  |  | SI | Before procedure |
| Q66 | numeric |  |  | SI | 1st addition |
| Q67 | numeric |  |  | SI | 2nd addition |
| Q68 | numeric |  |  | SI | After procedure |
| Q69 | varchar |  |  | SI | Pack(s) |
| Q70 | numeric |  |  | SI | Before procedure |
| Q71 | numeric |  |  | SI | 1st addition |
| Q72 | numeric |  |  | SI | 2nd addition |
| Q73 | numeric |  |  | SI | After procedure |
| Q74 | varchar |  |  | SI | Swab(s) |
| Q75 | numeric |  |  | SI | Before procedure |
| Q76 | numeric |  |  | SI | 1st addition |
| Q77 | numeric |  |  | SI | 2nd addition |
| Q78 | numeric |  |  | SI | After procedure |
| Q79 | varchar |  |  | SI | Suture Needle(s) |
| Q80 | numeric |  |  | SI | Before procedure |
| Q81 | numeric |  |  | SI | 1st addition |
| Q82 | numeric |  |  | SI | 2nd addition |
| Q83 | numeric |  |  | SI | After procedure |
| Q84 | varchar |  |  | SI | Syringe Needle(s) |
| Q85 | numeric |  |  | SI | Before procedure |
| Q86 | numeric |  |  | SI | 1st addition |
| Q87 | numeric |  |  | SI | 2nd addition |
| Q88 | numeric |  |  | SI | After procedure |
| Q89 | varchar |  |  | SI | Sponge(s) |
| Q90 | numeric |  |  | SI | Before procedure |
| Q91 | numeric |  |  | SI | 1st addition |
| Q92 | numeric |  |  | SI | 2nd addition |
| Q93 | numeric |  |  | SI | After procedure |
| Q94 | varchar |  |  | SI | Tampon(s) |
| Q95 | numeric |  |  | SI | Before procedure |
| Q96 | numeric |  |  | SI | 1st addition |
| Q97 | numeric |  |  | SI | 2nd addition |
| Q98 | numeric |  |  | SI | After procedure |
| Q99 | varchar |  |  | SI | Intentionally Retained Items In Situ |
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