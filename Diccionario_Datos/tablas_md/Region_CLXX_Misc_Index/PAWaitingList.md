# Region_CLXX_Misc_Index.PAWaitingList

**Schema:** Region_CLXX_Misc_Index
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Personalización Regional Chile**. Adaptaciones y extensiones locales del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreateTimeStamp | timestamp |  |  | SI | Time stamp of record creation |
| CreateUserDR | bigint |  | FK | SI | TrakCare User |
| DateFrom | date |  |  | NO | - |
| DateTo | date |  |  | SI | - |
| EpisodeDR | bigint |  | FK | NO | Des Ref PAADM |
| ParentWardDR | bigint |  | FK | NO | Des Ref PACWard |
| TimeFrom | time |  |  | NO | - |
| TimeTo | time |  |  | SI | - |
| UpdateTimeStamp | timestamp |  |  | SI | Time stamp of record update |
| UpdateUserDR | bigint |  | FK | SI | TrakCare User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*