# SQLUser.BLC_MultOperDisc

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MULTOP_RowId | bigint | PK |  | NO | - |
| MULTOP_CreatedDate | date |  |  | SI | Created Date |
| MULTOP_CreatedTime | time |  |  | SI | Created Time |
| MULTOP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MULTOP_DateFrom | date |  |  | SI | Date From |
| MULTOP_DateTo | date |  |  | SI | Date To |
| MULTOP_Perc | double |  |  | SI | % Discount |
| MULTOP_UpdatedDate | date |  |  | SI | Updated Date |
| MULTOP_UpdatedTime | time |  |  | SI | Updated Time |
| MULTOP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Tipo de Afasia |
| Q03 | - |  |  | SI | Grado Afasia |
| Q04 | - |  |  | SI | Tiempo de Evolución |
| Q05 | - |  |  | SI | Lateralidad |
| Q06 | - |  |  | SI | Escolaridad |
| Q07 | - |  |  | SI | Etiología |
| Q08 | - |  |  | SI | Hemisferio |
| Q09 | - |  |  | SI | Hemiparesia |
| Q10 | - |  |  | SI | Det. Intel |
| Q11 | - |  |  | SI | N° PICA |
| Q12 | - |  |  | SI | 1. Palmera(1)* (3)** (Repetición) |
| Q13 | - |  |  | SI | 2. Chocolate(45)(4) (Repetición) |
| Q14 | - |  |  | SI | 3. Espárrago(1)(4) (Repetición) |
| Q15 | - |  |  | SI | 4. Helicóptero(4)(5) (Repetición) |
| Q16 | - |  |  | SI | 5. Rinoceronte(2) (Repetición) |
| Q17 | - |  |  | SI | 6. Pantufla(1)(3) (Repetición) |
| Q18 | - |  |  | SI | 7. Leopardo (2)(3) (Repetición) |
| Q19 | - |  |  | SI | 8. Calcetín(6)(4) (Repetición) |
| Q20 | - |  |  | SI | 9. Ternero(1)(3) (Repetición) |
| Q21 | - |  |  | SI | 10. Pollera(74)(3) (Repetición) |
| Q22 | - |  |  | SI | 11. Berenjena(84)(4) (Repetición) |
| Q23 | - |  |  | SI | 12. Ametralladora(3)(6) (Repetición) |
| Q24 | - |  |  | SI | 13. Avestruz(8)(3) (Repetición) |
| Q25 | - |  |  | SI | 14. Completo(143)(3) (Repetición) |
| Q26 | - |  |  | SI | 15. Destornillador(1)(5) (Repetición) |
| Q27 | - |  |  | SI | 16. Frutilla(8)(3) (Repetición) |
| Q28 | - |  |  | SI | 17. Ambulancia(5)(4) (Repetición) |
| Q29 | - |  |  | SI | 18. Langosta(7)(3) (Repetición) |
| Q30 | - |  |  | SI | 19. Velero (2) (3) (Repetición) |
| Q31 | - |  |  | SI | 20. Oreja (69) (3) (Repetición) |
| Q32 | - |  |  | SI | 1. Palmera(1)* (3)** (Comprensión Auditiva) |
| Q33 | - |  |  | SI | 2. Chocolate(45)(4) (Comprensión Auditiva) |
| Q34 | - |  |  | SI | 3. Espárrago(1)(4) (Comprensión Auditiva) |
| Q35 | - |  |  | SI | 4. Helicóptero(4)(5) (Comprensión Auditiva) |
| Q36 | - |  |  | SI | 5. Rinoceronte(2) (Comprensión Auditiva) |
| Q37 | - |  |  | SI | 6. Pantufla(1)(3) (Comprensión Auditiva) |
| Q38 | - |  |  | SI | 7. Leopardo (2)(3) (Comprensión Auditiva) |
| Q39 | - |  |  | SI | 8. Calcetín(6)(4) (Comprensión Auditiva) |
| Q40 | - |  |  | SI | 9. Ternero(1)(3) (Comprensión Auditiva) |
| Q41 | - |  |  | SI | 10. Pollera(74)(3) (Comprensión Auditiva) |
| Q42 | - |  |  | SI | 11. Berenjena(84)(4) (Comprensión Auditiva) |
| Q43 | - |  |  | SI | 12. Ametralladora(3)(6) (Comprensión Auditiva) |
| Q44 | - |  |  | SI | 13. Avestruz(8)(3) (Comprensión Auditiva) |
| Q45 | - |  |  | SI | 14. Completo(143)(3) (Comprensión Auditiva) |
| Q46 | - |  |  | SI | 15. Destornillador(1)(5) (Comprensión Auditiva) |
| Q47 | - |  |  | SI | 16. Frutilla(8)(3) (Comprensión Auditiva) |
| Q48 | - |  |  | SI | 17. Ambulancia(5)(4) (Comprensión Auditiva) |
| Q49 | - |  |  | SI | 18. Langosta(7)(3) (Comprensión Auditiva) |
| Q50 | - |  |  | SI | 19. Velero (2) (3) (Comprensión Auditiva) |
| Q51 | - |  |  | SI | 20. Oreja (69) (3) (Comprensión Auditiva) |
| Q52 | - |  |  | SI | Total (Repetición) |
| Q53 | - |  |  | SI | Total (Comprensión Auditiva) |
| Q54 | - |  |  | SI | Tiempo Total |
| Q55 | - |  |  | SI | Observaciones |
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