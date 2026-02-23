# questionnaire.QGXXXOPHT02

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date | PK |  | SI | HX Date |
| Q02 | varchar | PK |  | SI | Hx Type Brand OD |
| Q03 | varchar | PK |  | SI | Hx BC OD |
| Q04 | varchar | PK |  | SI | Hx Sph OD |
| Q05 | varchar | PK |  | SI | Hx Cyl OD |
| Q06 | varchar | PK |  | SI | Hx Axis OD |
| Q07 | varchar | PK |  | SI | Hx Add OD |
| Q08 | varchar | PK |  | SI | Hx VA-Dt OD |
| Q09 | varchar | PK |  | SI | Hx VA-Nr OD |
| Q10 | varchar | PK |  | SI | Hx Type Brand OS |
| Q11 | varchar | PK |  | SI | Hx BC OS |
| Q12 | varchar | PK |  | SI | Hx Sph OS |
| Q13 | varchar | PK |  | SI | Hx Cyl OS |
| Q14 | varchar | PK |  | SI | Hx Axis OS |
| Q15 | varchar | PK |  | SI | Hx Add OS |
| Q16 | varchar | PK |  | SI | Hx VA-Dt-OS |
| Q17 | varchar | PK |  | SI | Hx VA-Nr-OS |
| Q18 | varchar | PK |  | SI | Hx VA-Dt-OU |
| Q19 | varchar | PK |  | SI | Hx VA-Nr-OU |
| Q20 | varchar | PK |  | SI | Notes |
| Q21 | date | PK |  | SI | FX Date |
| Q22 | varchar | PK |  | SI | Fx Type Brand OD |
| Q23 | varchar | PK |  | SI | Fx BC OD |
| Q24 | varchar | PK |  | SI | Fx Sph OD |
| Q25 | varchar | PK |  | SI | Fx Cyl OD |
| Q26 | varchar | PK |  | SI | Fx Axis OD |
| Q27 | varchar | PK |  | SI | Fx Add OD |
| Q28 | varchar | PK |  | SI | Fx VA-Dt OD |
| Q29 | varchar | PK |  | SI | Fx VA-Nr OD |
| Q30 | varchar | PK |  | SI | Fx Type Brand OS |
| Q31 | varchar | PK |  | SI | Fx BC OS |
| Q32 | varchar | PK |  | SI | Fx Sph OS |
| Q33 | varchar | PK |  | SI | Fx Cyl OS |
| Q34 | varchar | PK |  | SI | Fx Axis OS |
| Q35 | varchar | PK |  | SI | Fx Add OS |
| Q36 | varchar | PK |  | SI | Fx VA-Dt-OS |
| Q37 | varchar | PK |  | SI | Fx VA-Nr-OS |
| Q38 | varchar | PK |  | SI | Fx VA-Dt-OU |
| Q39 | varchar | PK |  | SI | Fx VA-Nr-OU |
| Q40 | varchar | PK |  | SI | Notes |
| Q41 | varchar | PK |  | SI | UC VA-Dt OD |
| Q42 | varchar | PK |  | SI | UC VA-Nr OD |
| Q43 | varchar | PK |  | SI | UC VA-Dt OS |
| Q44 | varchar | PK |  | SI | UC VA-Nr OS |
| Q45 | varchar | PK |  | SI | UC VA-Dt OU |
| Q46 | varchar | PK |  | SI | UC VA-Nr OU |
| Q47 | varchar | PK |  | SI | VAUC Notes |
| Q48 | varchar | PK |  | SI | C VA-Dt OD |
| Q49 | varchar | PK |  | SI | C VA-Nr OD |
| Q50 | varchar | PK |  | SI | C VA-Dt OS |
| Q51 | varchar | PK |  | SI | C VA-Nr OS |
| Q52 | varchar | PK |  | SI | C VA-Dt OU |
| Q53 | varchar | PK |  | SI | C VA-Nr OU |
| Q54 | varchar | PK |  | SI | VA C Notes |
| Q55 | varchar | PK |  | SI | BC VA-Dt OD |
| Q56 | varchar | PK |  | SI | BC VA-Nr OD |
| Q57 | varchar | PK |  | SI | BC VA-Dt OS |
| Q58 | varchar | PK |  | SI | BC VA-Nr OS |
| Q59 | varchar | PK |  | SI | BC VA-Dt OU |
| Q60 | varchar | PK |  | SI | BC VA-Nr OU |
| Q61 | varchar | PK |  | SI | VA BC Notes |
| Q62 | varchar | PK |  | SI | Hx VA-Nr-OU |
| Q63 | varchar | PK |  | SI | Hx VA-Dt-OU |
| Q64 | varchar | PK |  | SI | VABC Notes |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*