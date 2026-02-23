# questionnaire.QTCECSIH

> Cuestionario de Salud Infantil 5 - 9 Años (Hombres)

**Schema:** questionnaire
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario de Salud Infantil 5 - 9 Años (Hombres)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre de la Madre  |
| Q02 | varchar |  |  | SI | Colegio  |
| Q03 | varchar |  |  | SI | Curso |
| Q04 | varchar |  |  | SI | Peso |
| Q04ObsDR | varchar |  | FK | SI | Peso DR |
| Q05 | varchar |  |  | SI | Talla |
| Q05ObsDR | varchar |  | FK | SI | Talla DR |
| Q06 | numeric |  |  | SI | IMC |
| Q07 | varchar |  |  | SI | IMC (Calculado) |
| Q08 | varchar |  |  | SI | Circunferencia Abdominal |
| Q08ObsDR | varchar |  | FK | SI | Circunferencia Abdominal DR |
| Q09 | varchar |  |  | SI | Percentil IMC - Edad |
| Q09ObsDR | varchar |  | FK | SI | Percentil IMC - Edad DR |
| Q10 | varchar |  |  | SI | Percentil Talla - Edad |
| Q10ObsDR | varchar |  | FK | SI | Percentil Talla - Edad DR |
| Q11 | varchar |  |  | SI | Percentil de Circunferencia Abdominal |
| Q11ObsDR | varchar |  | FK | SI | Percentil de Circunferencia Abdominal DR |
| Q12 | varchar |  |  | SI | Tanner Genitales |
| Q12ObsDR | varchar |  | FK | SI | Tanner Genitales DR |
| Q13 | varchar |  |  | SI | Tanner Vello Púbico |
| Q13ObsDR | varchar |  | FK | SI | Tanner Vello Púbico DR |
| Q14 | varchar |  |  | SI | 1. ¿No controla el pipí de día o de noche, aunque ... |
| Q15 | varchar |  |  | SI | 2. ¿Se queja de dolor frecuente al hacer pipí? |
| Q16 | varchar |  |  | SI | 3. ¿No controla deposiciones (caca) de día o de no... |
| Q17 | varchar |  |  | SI | 4. ¿Actualmente tiene parásitos (gusanos) en sus d... |
| Q18 | varchar |  |  | SI | 5. ¿Mancha los calzoncillos con secreción o deposi... |
| Q19 | varchar |  |  | SI | 6. ¿Tiene picazón anal frecuente? |
| Q20 | varchar |  |  | SI | 7. ¿Tiene secreción de muy mal olor en el pene, pi... |
| Q21 | varchar |  |  | SI | 8. ¿La piel que recubre el pene es estrecha y no p... |
| Q22 | varchar |  |  | SI | 9. ¿Uno o ambos testículos están ausentes en escro... |
| Q23 | varchar |  |  | SI | 10. ¿Tiene un aumento de volumen (hinchazón) en la... |
| Q24 | varchar |  |  | SI | 11. ¿Tiene olor axilar similar al de un adulto (Es... |
| Q25 | varchar |  |  | SI | 12. ¿Ha tenido sibilancias o silbido al pecho en e... |
| Q26 | varchar |  |  | SI | 13. ¿Ha tenido sibilancias o silbido al pecho dura... |
| Q27 | varchar |  |  | SI | 14. ¿Ronca de noche?  |
| Q28 | varchar |  |  | SI | 15. Si ronca de noche ¿tiene pausas respiratorias?... |
| Q29 | varchar |  |  | SI | 16. ¿Tiene actualmente piojos en su pelo?  |
| Q30 | varchar |  |  | SI | Alguna otra inquietud manifestada por el padre/mad... |
| Q31 | varchar |  |  | SI | Perímetro de Cintura |
| Q31ObsDR | varchar |  | FK | SI | Perímetro de Cintura DR |
| Q32 | varchar |  |  | SI | IMC por Edad |
| Q32ObsDR | varchar |  | FK | SI | IMC por Edad DR |
| Q33 | varchar |  |  | SI | Peso por Edad |
| Q33ObsDR | varchar |  | FK | SI | Peso por Edad DR |
| Q34 | varchar |  |  | SI | Talla por Edad |
| Q34ObsDR | varchar |  | FK | SI | Talla por Edad DR |
| Q35 | varchar |  |  | SI | Puntaje Z IMC por Edad |
| Q35ObsDR | varchar |  | FK | SI | Puntaje Z IMC por Edad DR |
| Q36 | varchar |  |  | SI | Puntaje Z Peso por Edad |
| Q36ObsDR | varchar |  | FK | SI | Puntaje Z Peso por Edad DR |
| Q37 | varchar |  |  | SI | Puntaje Z Talla por Edad |
| Q37ObsDR | varchar |  | FK | SI | Puntaje Z Talla por Edad DR |
| Q38 | varchar |  |  | SI | Calificación Estatura |
| Q38ObsDR | varchar |  | FK | SI | Calificación Estatura DR |
| Q39 | varchar |  |  | SI | Estatura Padre |
| Q39ObsDR | varchar |  | FK | SI | Estatura Padre DR |
| Q40 | varchar |  |  | SI | Estatura Madre |
| Q40ObsDR | varchar |  | FK | SI | Estatura Madre DR |
| Q41 | varchar |  |  | SI | Talla Diana Hombres |
| Q42 | varchar |  |  | SI | Talla Diana Mujeres |
| Q43 | varchar |  |  | SI | Diagnóstico Nutricional |
| Q43ObsDR | varchar |  | FK | SI | Diagnóstico Nutricional DR |
| Q44 | varchar |  |  | SI | Obesidad Abdominal según Cirunferencia de Cintura |
| Q44ObsDR | varchar |  | FK | SI | Obesidad Abdominal según Cirunferencia de Cintura ... |
| Q45 | varchar |  |  | SI | Índice Cintura/Estatura |
| Q46 | bit |  |  | SI | Ingresar Información en forma manual |
| Q47 | varchar |  |  | SI | P.A.Sistólica |
| Q47ObsDR | varchar |  | FK | SI | P.A.Sistólica DR |
| Q48 | varchar |  |  | SI | P.A. Diastólica |
| Q48ObsDR | varchar |  | FK | SI | P.A. Diastólica DR |
| Q49 | varchar |  |  | SI | Percentil PAS |
| Q50 | varchar |  |  | SI | Percentil PAD |
| Q54 | varchar |  |  | SI | Examen Físico |
| Q55 | varchar |  |  | SI | Cabeza y cuello |
| Q56 | varchar |  |  | SI | Tórax |
| Q57 | varchar |  |  | SI | Examen Cardíaco |
| Q58 | varchar |  |  | SI | Examen Pulmonar |
| Q59 | varchar |  |  | SI | Abdomen |
| Q60 | varchar |  |  | SI | Examen genital |
| Q61 | varchar |  |  | SI | Columna |
| Q62 | varchar |  |  | SI | Extremidades |
| QNNA01E | varchar |  |  | SI | Curso [REM] |
| QPNN | varchar |  |  | SI | Paciente NANEAS |
| QSEN | varchar |  |  | SI | Usuario bajo algún programa del SENAME [REM] |
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