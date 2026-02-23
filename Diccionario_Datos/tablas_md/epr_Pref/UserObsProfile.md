# epr_Pref.UserObsProfile

**Schema:** epr_Pref
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| UPREFExpandAttr | varchar |  |  | SI | Expand Attributes |
| UPREFHideEmptyRows | varchar |  |  | SI | Hide Observation Items If No Data |
| UPREFObsGroupDR | bigint |  | FK | SI | Observation Group
Restrict this preference for a ... |
| UPREFUpdateDate | date |  |  | SI | Last Updated Date |
| UPREFUpdateTime | time |  |  | SI | Last Updated Time |
| UPREFUpdateUserDR | bigint |  | FK | SI | Last Updated By User |
| UPREFUserDR | bigint |  | FK | NO | User
Preference applies to this user |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*