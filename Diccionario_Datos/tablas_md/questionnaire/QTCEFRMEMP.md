# questionnaire.QTCEFRMEMP

> Examen Anual de Medicina Preventiva Del Adulto Mayor (EMPAM)

**Schema:** questionnaire
**Columnas:** 191
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Anual de Medicina Preventiva Del Adulto Mayor (EMPAM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Peso |
| Q10 | bit |  |  | SI | Glibenclamida |
| Q100 | varchar |  |  | SI | Estado Nutricional |
| Q100ObsDR | varchar |  | FK | SI | Estado Nutricional DR |
| Q101 | varchar |  |  | SI | Clasificación Estación unipodal Izquierda |
| Q102 | varchar |  |  | SI | Clasificación Estación unipodal derecha |
| Q103 | varchar |  |  | SI | Resultado Indice Barthel |
| Q103ObsDR | varchar |  | FK | SI | Resultado Indice Barthel DR |
| Q104 | varchar |  |  | SI | Circunferencia Cintura |
| Q104ObsDR | varchar |  | FK | SI | Circunferencia Cintura DR |
| Q105 | varchar |  |  | SI | 3 veces por semana mínimo 30 min. de duración |
| Q107 | varchar |  |  | SI | Adulto Mayor Institucionalizado (antiguo) |
| Q108 | varchar |  |  | SI | Displasia Bronco-Pulmonar |
| Q108ObsDR | varchar |  | FK | SI | Displasia Bronco-Pulmonar DR |
| Q11 | bit |  |  | SI | Metformina |
| Q110 | varchar |  |  | SI | Estado Nutricional PACAM |
| Q110ObsDR | varchar |  | FK | SI | Estado Nutricional PACAM DR |
| Q12 | bit |  |  | SI | Tolbutamida |
| Q13 | bit |  |  | SI | Nifedipino |
| Q134 | varchar |  |  | SI | Resultado AUDIT |
| Q134ObsDR | varchar |  | FK | SI | Resultado AUDIT DR |
| Q14 | bit |  |  | SI | Atenolol |
| Q15 | bit |  |  | SI | Insulina |
| Q16 | bit |  |  | SI | Propanolol |
| Q17 | bit |  |  | SI | Furosemida |
| Q18 | bit |  |  | SI | Losartan |
| Q181 | varchar |  |  | SI | Pulso |
| Q181ObsDR | varchar |  | FK | SI | Pulso DR |
| Q182 | varchar |  |  | SI | Realiza Act. Física |
| Q183 | varchar |  |  | SI | Tiene quien lo Apoye? |
| Q184 | varchar |  |  | SI | Ayuda |
| Q185 | numeric |  |  | SI | Derecha |
| Q186 | numeric |  |  | SI | Izquierda |
| Q187 | varchar |  |  | SI | TIME UP AND GO |
| Q19 | bit |  |  | SI | Enalapril |
| Q190 | varchar |  |  | SI | Indice de Katz |
| Q190ObsDR | varchar |  | FK | SI | Indice de Katz DR |
| Q194 | varchar |  |  | SI | Maltrato |
| Q195 | varchar |  |  | SI | Glicemia |
| Q195ObsDR | varchar |  | FK | SI | Glicemia DR |
| Q196 | varchar |  |  | SI | Tabaquismo |
| Q197 | bit |  |  | SI | HTA |
| Q198 | bit |  |  | SI | DM |
| Q199 | bit |  |  | SI | Dislipidemia |
| Q1ObsDR | varchar |  | FK | SI | Peso DR |
| Q2 | varchar |  |  | SI | Talla |
| Q20 | bit |  |  | SI | Hidroclorotiazida |
| Q200 | bit |  |  | SI | Obesidad |
| Q201 | bit |  |  | SI | Desnutrición |
| Q202 | bit |  |  | SI | Hipotiroidismo |
| Q203 | bit |  |  | SI | Neumonia |
| Q204 | bit |  |  | SI | EPOC |
| Q205 | bit |  |  | SI | Depresión |
| Q206 | bit |  |  | SI | Demencia |
| Q207 | bit |  |  | SI | AVC |
| Q208 | bit |  |  | SI | Parkinson |
| Q209 | bit |  |  | SI | Caídas Frecuentes |
| Q21 | bit |  |  | SI | Diazepan |
| Q210 | bit |  |  | SI | Hipoacusia |
| Q211 | bit |  |  | SI | Artrosis |
| Q212 | bit |  |  | SI | Artritis Reumatoidea |
| Q213 | bit |  |  | SI | Ceguera,Baja Visión |
| Q214 | bit |  |  | SI | Incontinencia Urinaria |
| Q215 | bit |  |  | SI | Inmovilismo |
| Q216 | bit |  |  | SI | Secuela AVC |
| Q217 | bit |  |  | SI | Levadopa |
| Q218 | bit |  |  | SI | EMP Anual |
| Q219 | bit |  |  | SI | Orientar a Grupos de la Comunidad |
| Q22 | bit |  |  | SI | Fluoxetina |
| Q220 | bit |  |  | SI | Cardiovascular Educación  |
| Q221 | bit |  |  | SI | Derivar Médico Educación |
| Q222 | bit |  |  | SI | Derivar Médico Educación |
| Q223 | bit |  |  | SI | Derivar Médico Educación |
| Q224 | bit |  |  | SI | Derivar a Médico  |
| Q225 | bit |  |  | SI | Derivar a Centro de Rehabilitación |
| Q226 | bit |  |  | SI | Atención Domiciliaria |
| Q227 | varchar |  |  | SI | Otras Indicaciones |
| Q228 | date |  |  | SI | Fecha de vigencia |
| Q229 | varchar |  |  | SI | Resultado de Escala de Depresión Geriátrica |
| Q229ObsDR | varchar |  | FK | SI | Resultado de Escala de Depresión Geriátrica DR |
| Q23 | bit |  |  | SI | Sertralina |
| Q230 | varchar |  |  | SI | Resultado actividades funcionales Pfeffer |
| Q230ObsDR | varchar |  | FK | SI | Resultado actividades funcionales Pfeffer DR |
| Q231 | bit |  |  | SI | Familia |
| Q232 | bit |  |  | SI | Amigos |
| Q233 | bit |  |  | SI | Vecinos |
| Q234 | bit |  |  | SI | Grupos Organizados |
| Q24 | bit |  |  | SI | Salbutamol |
| Q25 | bit |  |  | SI | Inflamide |
| Q26 | bit |  |  | SI | Aspirina |
| Q27 | bit |  |  | SI | Paracetamol |
| Q28 | bit |  |  | SI | Diclofenaco |
| Q29 | bit |  |  | SI | Tramadol |
| Q2ObsDR | varchar |  | FK | SI | Talla DR |
| Q3 | varchar |  |  | SI | Índice de Masa Corporal (IMC) |
| Q30 | bit |  |  | SI | Celecoxib |
| Q300 | varchar |  |  | SI | Descripción Otros Medicamentos |
| Q31 | bit |  |  | SI | Omeprazol |
| Q4 | varchar |  |  | SI | Clasificación de C. Cintura |
| Q43 | varchar |  |  | SI | Resultado EFAM A |
| Q43ObsDR | varchar |  | FK | SI | Resultado EFAM A DR |
| Q45 | varchar |  |  | SI | Resultado EFAM B |
| Q45ObsDR | varchar |  | FK | SI | Resultado EFAM B DR |
| Q46 | bit |  |  | SI | Otras observaciones al aplicar EFAM  |
| Q47 | bit |  |  | SI | Mareos |
| Q48 | bit |  |  | SI | Temblor de reposo |
| Q49 | bit |  |  | SI | Alteración del equilibrio |
| Q50 | bit |  |  | SI | Dolor de cadera |
| Q51 | bit |  |  | SI | Dolor de rodilla |
| Q52 | bit |  |  | SI | Dolor de hombro |
| Q53 | bit |  |  | SI | Dolor de espalda |
| Q54 | bit |  |  | SI | Alteración visual |
| Q55 | bit |  |  | SI | Alteración auditiva |
| Q56 | bit |  |  | SI | Otro |
| Q57 | varchar |  |  | SI | Especifique otra |
| Q63 | varchar |  |  | SI | Clasificación |
| Q7 | varchar |  |  | SI | Presión arterial (mmHg) Diastólica sentado |
| Q7ObsDR | varchar |  | FK | SI | Presión arterial (mmHg) Diastólica sentado DR |
| Q7a | varchar |  |  | SI | Presión arterial (mmHg) Sistólica sentado |
| Q7aObsDR | varchar |  | FK | SI | Presión arterial (mmHg) Sistólica sentado DR |
| Q8 | varchar |  |  | SI | Presión arterial (mmHg) Diastólica de pie |
| Q8ObsDR | varchar |  | FK | SI | Presión arterial (mmHg) Diastólica de pie DR |
| Q8a | varchar |  |  | SI | Presión arterial (mmHg) Sistólica de pie |
| Q8aObsDR | varchar |  | FK | SI | Presión arterial (mmHg) Sistólica de pie DR |
| Q99 | varchar |  |  | SI | Plan Maltrato |
| QAFI | varchar |  |  | SI |  Adulto Mayor Institucionalizado |
| QAFIObsDR | varchar |  | FK | SI |  Adulto Mayor Institucionalizado DR |
| QOTM | bit |  |  | SI | Otro Medicamento |
| QR01 | varchar |  |  | SI | Resultado EFAM A |
| QR02 | varchar |  |  | SI | Resultado EFAM B |
| QR03 | varchar |  |  | SI | Resultado Escala de Depresión Geriátrica |
| QR04 | varchar |  |  | SI | Resultado Índice de Barthel |
| QR05 | varchar |  |  | SI | Resultado AUDIT-C |
| QR06 | varchar |  |  | SI | Resultado AUDIT |
| QR07 | varchar |  |  | SI | Resultado Actividades Funcionales Pfeffer |
| QR08 | varchar |  |  | SI | Resultado Minimental Extendido |
| QR117 | varchar |  |  | SI | Baja de peso involuntariamente en los últimos 6 me... |
| QR118 | varchar |  |  | SI | Observaciones de las mediciones |
| QR118N | varchar |  |  | SI | Observaciones de las mediciones |
| QR120 | varchar |  |  | SI | Paciente pertenece a PACAM |
| QR121 | varchar |  |  | SI | Prueba de Elisa |
| QR121ObsDR | varchar |  | FK | SI | Prueba de Elisa DR |
| QR124 | varchar |  |  | SI | ASSIST |
| QR125 | varchar |  |  | SI | Resultado CRAFFT |
| QRB | varchar |  |  | SI | RBaci |
| QRBObsDR | varchar |  | FK | SI | RBaci DR |
| QRCT | varchar |  |  | SI | CT |
| QRCTObsDR | varchar |  | FK | SI | CT DR |
| QRVDRL | varchar |  |  | SI | VDRL |
| QRVDRLObsDR | varchar |  | FK | SI | VDRL DR |
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