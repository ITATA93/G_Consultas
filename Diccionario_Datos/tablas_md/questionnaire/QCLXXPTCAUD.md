# questionnaire.QCLXXPTCAUD

> Protocolo Test Comprensión Audición y Repetición

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Protocolo Test Comprensión Audición y Repetición

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | varchar |  |  | SI | Tipo de Afasia |
| Q03 | varchar |  |  | SI | Grado Afasia |
| Q04 | varchar |  |  | SI | Tiempo de Evolución |
| Q05 | varchar |  |  | SI | Lateralidad |
| Q06 | varchar |  |  | SI | Escolaridad |
| Q07 | varchar |  |  | SI | Etiología |
| Q08 | varchar |  |  | SI | Hemisferio |
| Q09 | varchar |  |  | SI | Hemiparesia |
| Q10 | varchar |  |  | SI | Det. Intel |
| Q11 | varchar |  |  | SI | N° PICA |
| Q12 | varchar |  |  | SI | 1. Palmera(1)* (3)** (Repetición) |
| Q13 | varchar |  |  | SI | 2. Chocolate(45)(4) (Repetición) |
| Q14 | varchar |  |  | SI | 3. Espárrago(1)(4) (Repetición) |
| Q15 | varchar |  |  | SI | 4. Helicóptero(4)(5) (Repetición) |
| Q16 | varchar |  |  | SI | 5. Rinoceronte(2) (Repetición) |
| Q17 | varchar |  |  | SI | 6. Pantufla(1)(3) (Repetición) |
| Q18 | varchar |  |  | SI | 7. Leopardo (2)(3) (Repetición) |
| Q19 | varchar |  |  | SI | 8. Calcetín(6)(4) (Repetición) |
| Q20 | varchar |  |  | SI | 9. Ternero(1)(3) (Repetición) |
| Q21 | varchar |  |  | SI | 10. Pollera(74)(3) (Repetición) |
| Q22 | varchar |  |  | SI | 11. Berenjena(84)(4) (Repetición) |
| Q23 | varchar |  |  | SI | 12. Ametralladora(3)(6) (Repetición) |
| Q24 | varchar |  |  | SI | 13. Avestruz(8)(3) (Repetición) |
| Q25 | varchar |  |  | SI | 14. Completo(143)(3) (Repetición) |
| Q26 | varchar |  |  | SI | 15. Destornillador(1)(5) (Repetición) |
| Q27 | varchar |  |  | SI | 16. Frutilla(8)(3) (Repetición) |
| Q28 | varchar |  |  | SI | 17. Ambulancia(5)(4) (Repetición) |
| Q29 | varchar |  |  | SI | 18. Langosta(7)(3) (Repetición) |
| Q30 | varchar |  |  | SI | 19. Velero (2) (3) (Repetición) |
| Q31 | varchar |  |  | SI | 20. Oreja (69) (3) (Repetición) |
| Q32 | varchar |  |  | SI | 1. Palmera(1)* (3)** (Comprensión Auditiva) |
| Q33 | varchar |  |  | SI | 2. Chocolate(45)(4) (Comprensión Auditiva) |
| Q34 | varchar |  |  | SI | 3. Espárrago(1)(4) (Comprensión Auditiva) |
| Q35 | varchar |  |  | SI | 4. Helicóptero(4)(5) (Comprensión Auditiva) |
| Q36 | varchar |  |  | SI | 5. Rinoceronte(2) (Comprensión Auditiva) |
| Q37 | varchar |  |  | SI | 6. Pantufla(1)(3) (Comprensión Auditiva) |
| Q38 | varchar |  |  | SI | 7. Leopardo (2)(3) (Comprensión Auditiva) |
| Q39 | varchar |  |  | SI | 8. Calcetín(6)(4) (Comprensión Auditiva) |
| Q40 | varchar |  |  | SI | 9. Ternero(1)(3) (Comprensión Auditiva) |
| Q41 | varchar |  |  | SI | 10. Pollera(74)(3) (Comprensión Auditiva) |
| Q42 | varchar |  |  | SI | 11. Berenjena(84)(4) (Comprensión Auditiva) |
| Q43 | varchar |  |  | SI | 12. Ametralladora(3)(6) (Comprensión Auditiva) |
| Q44 | varchar |  |  | SI | 13. Avestruz(8)(3) (Comprensión Auditiva) |
| Q45 | varchar |  |  | SI | 14. Completo(143)(3) (Comprensión Auditiva) |
| Q46 | varchar |  |  | SI | 15. Destornillador(1)(5) (Comprensión Auditiva) |
| Q47 | varchar |  |  | SI | 16. Frutilla(8)(3) (Comprensión Auditiva) |
| Q48 | varchar |  |  | SI | 17. Ambulancia(5)(4) (Comprensión Auditiva) |
| Q49 | varchar |  |  | SI | 18. Langosta(7)(3) (Comprensión Auditiva) |
| Q50 | varchar |  |  | SI | 19. Velero (2) (3) (Comprensión Auditiva) |
| Q51 | varchar |  |  | SI | 20. Oreja (69) (3) (Comprensión Auditiva) |
| Q52 | numeric |  |  | SI | Total (Repetición) |
| Q53 | numeric |  |  | SI | Total (Comprensión Auditiva) |
| Q54 | numeric |  |  | SI | Tiempo Total |
| Q55 | varchar |  |  | SI | Observaciones |
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