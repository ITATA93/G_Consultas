# SQLUser.AR_PatBillGroupChargeObserv

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | varchar | PK |  | NO | AR_PatBillGroupCharges Parent Reference |
| ChildQ12DR | - |  |  | SI | Child Reference: Dispositivos Neuromonitoreo |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_Date | date |  |  | SI | Date |
| OBS_ObservValueMultiLineText | varchar |  |  | SI | Observation Value Multi Line Text |
| OBS_ObservationCode | varchar |  |  | SI | Observation Code |
| OBS_ObservationType_DR | bigint |  | FK | SI | Des Ref to ARCObservationType |
| OBS_ObservationValue | varchar |  |  | SI | Observation Value |
| OBS_ObservationValueText | varchar |  |  | SI | Observation Value Text |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_Time | time |  |  | SI | Time |
| Q10Q1 | - |  |  | SI | Tipo Drenajes |
| Q10Q10 | - |  |  | SI | ¿Es Necesario el DI? |
| Q10Q2 | - |  |  | SI | Subtipo |
| Q10Q3 | - |  |  | SI | Tamaño |
| Q10Q4 | - |  |  | SI | Actividad |
| Q10Q5 | - |  |  | SI | Ubicación |
| Q10Q6 | - |  |  | SI | Zona Inserción |
| Q10Q7 | - |  |  | SI | Descripción del Contenido |
| Q10Q8 | - |  |  | SI | Estado de la Cobertura |
| Q10Q9 | - |  |  | SI | N° Días de Drenaje |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*