# SQLUser.ARC_CashShiftAdjust

**Schema:** SQLUser
**Columnas:** 204
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CSAD_RowId | bigint | PK |  | NO | - |
| CSAD_Code | varchar |  |  | NO | Code |
| CSAD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CSAD_CreatedDate | date |  |  | SI | Created Date |
| CSAD_CreatedTime | time |  |  | SI | Created Time |
| CSAD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CSAD_DateFrom | date |  |  | SI | Date From |
| CSAD_DateTo | date |  |  | SI | Date To |
| CSAD_Desc | varchar |  |  | NO | Description |
| CSAD_Owner | varchar |  |  | SI | Owner |
| CSAD_UpdatedDate | date |  |  | SI | Updated Date |
| CSAD_UpdatedTime | time |  |  | SI | Updated Time |
| CSAD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQR119DR | - |  |  | SI | Child Reference: Vacunación del Adulto Mayor |
| Q1 | - |  |  | SI | Peso |
| Q10 | - |  |  | SI | Glibenclamida |
| Q100 | - |  |  | SI | Estado Nutricional |
| Q100ObsDR | - |  |  | SI | Estado Nutricional DR |
| Q101 | - |  |  | SI | Clasificación Estación unipodal Izquierda |
| Q102 | - |  |  | SI | Clasificación Estación unipodal derecha |
| Q103 | - |  |  | SI | Resultado Indice Barthel |
| Q103ObsDR | - |  |  | SI | Resultado Indice Barthel DR |
| Q104 | - |  |  | SI | Circunferencia Cintura |
| Q104ObsDR | - |  |  | SI | Circunferencia Cintura DR |
| Q105 | - |  |  | SI | 3 veces por semana mínimo 30 min. de duración |
| Q107 | - |  |  | SI | Adulto Mayor Institucionalizado (antiguo) |
| Q108 | - |  |  | SI | Displasia Bronco-Pulmonar |
| Q108ObsDR | - |  |  | SI | Displasia Bronco-Pulmonar DR |
| Q11 | - |  |  | SI | Metformina |
| Q110 | - |  |  | SI | Estado Nutricional PACAM |
| Q110ObsDR | - |  |  | SI | Estado Nutricional PACAM DR |
| Q12 | - |  |  | SI | Tolbutamida |
| Q13 | - |  |  | SI | Nifedipino |
| Q134 | - |  |  | SI | Resultado AUDIT |
| Q134ObsDR | - |  |  | SI | Resultado AUDIT DR |
| Q14 | - |  |  | SI | Atenolol |
| Q15 | - |  |  | SI | Insulina |
| Q16 | - |  |  | SI | Propanolol |
| Q17 | - |  |  | SI | Furosemida |
| Q18 | - |  |  | SI | Losartan |
| Q181 | - |  |  | SI | Pulso |
| Q181ObsDR | - |  |  | SI | Pulso DR |
| Q182 | - |  |  | SI | Realiza Act. Física |
| Q183 | - |  |  | SI | Tiene quien lo Apoye? |
| Q184 | - |  |  | SI | Ayuda |
| Q185 | - |  |  | SI | Derecha |
| Q186 | - |  |  | SI | Izquierda |
| Q187 | - |  |  | SI | TIME UP AND GO |
| Q19 | - |  |  | SI | Enalapril |
| Q190 | - |  |  | SI | Indice de Katz |
| Q190ObsDR | - |  |  | SI | Indice de Katz DR |
| Q194 | - |  |  | SI | Maltrato |
| Q195 | - |  |  | SI | Glicemia |
| Q195ObsDR | - |  |  | SI | Glicemia DR |
| Q196 | - |  |  | SI | Tabaquismo |
| Q197 | - |  |  | SI | HTA |
| Q198 | - |  |  | SI | DM |
| Q199 | - |  |  | SI | Dislipidemia |
| Q1ObsDR | - |  |  | SI | Peso DR |
| Q2 | - |  |  | SI | Talla |
| Q20 | - |  |  | SI | Hidroclorotiazida |
| Q200 | - |  |  | SI | Obesidad |
| Q201 | - |  |  | SI | Desnutrición |
| Q202 | - |  |  | SI | Hipotiroidismo |
| Q203 | - |  |  | SI | Neumonia |
| Q204 | - |  |  | SI | EPOC |
| Q205 | - |  |  | SI | Depresión |
| Q206 | - |  |  | SI | Demencia |
| Q207 | - |  |  | SI | AVC |
| Q208 | - |  |  | SI | Parkinson |
| Q209 | - |  |  | SI | Caídas Frecuentes |
| Q21 | - |  |  | SI | Diazepan |
| Q210 | - |  |  | SI | Hipoacusia |
| Q211 | - |  |  | SI | Artrosis |
| Q212 | - |  |  | SI | Artritis Reumatoidea |
| Q213 | - |  |  | SI | Ceguera,Baja Visión |
| Q214 | - |  |  | SI | Incontinencia Urinaria |
| Q215 | - |  |  | SI | Inmovilismo |
| Q216 | - |  |  | SI | Secuela AVC |
| Q217 | - |  |  | SI | Levadopa |
| Q218 | - |  |  | SI | EMP Anual |
| Q219 | - |  |  | SI | Orientar a Grupos de la Comunidad |
| Q22 | - |  |  | SI | Fluoxetina |
| Q220 | - |  |  | SI | Cardiovascular Educación |
| Q221 | - |  |  | SI | Derivar Médico Educación |
| Q222 | - |  |  | SI | Derivar Médico Educación |
| Q223 | - |  |  | SI | Derivar Médico Educación |
| Q224 | - |  |  | SI | Derivar a Médico |
| Q225 | - |  |  | SI | Derivar a Centro de Rehabilitación |
| Q226 | - |  |  | SI | Atención Domiciliaria |
| Q227 | - |  |  | SI | Otras Indicaciones |
| Q228 | - |  |  | SI | Fecha de vigencia |
| Q229 | - |  |  | SI | Resultado de Escala de Depresión Geriátrica |
| Q229ObsDR | - |  |  | SI | Resultado de Escala de Depresión Geriátrica DR |
| Q23 | - |  |  | SI | Sertralina |
| Q230 | - |  |  | SI | Resultado actividades funcionales Pfeffer |
| Q230ObsDR | - |  |  | SI | Resultado actividades funcionales Pfeffer DR |
| Q231 | - |  |  | SI | Familia |
| Q232 | - |  |  | SI | Amigos |
| Q233 | - |  |  | SI | Vecinos |
| Q234 | - |  |  | SI | Grupos Organizados |
| Q24 | - |  |  | SI | Salbutamol |
| Q25 | - |  |  | SI | Inflamide |
| Q26 | - |  |  | SI | Aspirina |
| Q27 | - |  |  | SI | Paracetamol |
| Q28 | - |  |  | SI | Diclofenaco |
| Q29 | - |  |  | SI | Tramadol |
| Q2ObsDR | - |  |  | SI | Talla DR |
| Q3 | - |  |  | SI | Índice de Masa Corporal (IMC) |
| Q30 | - |  |  | SI | Celecoxib |
| Q300 | - |  |  | SI | Descripción Otros Medicamentos |
| Q31 | - |  |  | SI | Omeprazol |
| Q4 | - |  |  | SI | Clasificación de C. Cintura |
| Q43 | - |  |  | SI | Resultado EFAM A |
| Q43ObsDR | - |  |  | SI | Resultado EFAM A DR |
| Q45 | - |  |  | SI | Resultado EFAM B |
| Q45ObsDR | - |  |  | SI | Resultado EFAM B DR |
| Q46 | - |  |  | SI | Otras observaciones al aplicar EFAM |
| Q47 | - |  |  | SI | Mareos |
| Q48 | - |  |  | SI | Temblor de reposo |
| Q49 | - |  |  | SI | Alteración del equilibrio |
| Q50 | - |  |  | SI | Dolor de cadera |
| Q51 | - |  |  | SI | Dolor de rodilla |
| Q52 | - |  |  | SI | Dolor de hombro |
| Q53 | - |  |  | SI | Dolor de espalda |
| Q54 | - |  |  | SI | Alteración visual |
| Q55 | - |  |  | SI | Alteración auditiva |
| Q56 | - |  |  | SI | Otro |
| Q57 | - |  |  | SI | Especifique otra |
| Q63 | - |  |  | SI | Clasificación |
| Q7 | - |  |  | SI | Presión arterial (mmHg) Diastólica sentado |
| Q7ObsDR | - |  |  | SI | Presión arterial (mmHg) Diastólica sentado DR |
| Q7a | - |  |  | SI | Presión arterial (mmHg) Sistólica sentado |
| Q7aObsDR | - |  |  | SI | Presión arterial (mmHg) Sistólica sentado DR |
| Q8 | - |  |  | SI | Presión arterial (mmHg) Diastólica de pie |
| Q8ObsDR | - |  |  | SI | Presión arterial (mmHg) Diastólica de pie DR |
| Q8a | - |  |  | SI | Presión arterial (mmHg) Sistólica de pie |
| Q8aObsDR | - |  |  | SI | Presión arterial (mmHg) Sistólica de pie DR |
| Q99 | - |  |  | SI | Plan Maltrato |
| QAFI | - |  |  | SI | Adulto Mayor Institucionalizado |
| QAFIObsDR | - |  |  | SI | Adulto Mayor Institucionalizado DR |
| QOTM | - |  |  | SI | Otro Medicamento |
| QR01 | - |  |  | SI | Resultado EFAM A |
| QR02 | - |  |  | SI | Resultado EFAM B |
| QR03 | - |  |  | SI | Resultado Escala de Depresión Geriátrica |
| QR04 | - |  |  | SI | Resultado Índice de Barthel |
| QR05 | - |  |  | SI | Resultado AUDIT-C |
| QR06 | - |  |  | SI | Resultado AUDIT |
| QR07 | - |  |  | SI | Resultado Actividades Funcionales Pfeffer |
| QR08 | - |  |  | SI | Resultado Minimental Extendido |
| QR117 | - |  |  | SI | Baja de peso involuntariamente en los últimos 6 me... |
| QR118 | - |  |  | SI | Observaciones de las mediciones |
| QR118N | - |  |  | SI | Observaciones de las mediciones |
| QR120 | - |  |  | SI | Paciente pertenece a PACAM |
| QR121 | - |  |  | SI | Prueba de Elisa |
| QR121ObsDR | - |  |  | SI | Prueba de Elisa DR |
| QR124 | - |  |  | SI | ASSIST |
| QR125 | - |  |  | SI | Resultado CRAFFT |
| QRB | - |  |  | SI | RBaci |
| QRBObsDR | - |  |  | SI | RBaci DR |
| QRCT | - |  |  | SI | CT |
| QRCTObsDR | - |  |  | SI | CT DR |
| QRVDRL | - |  |  | SI | VDRL |
| QRVDRLObsDR | - |  |  | SI | VDRL DR |
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