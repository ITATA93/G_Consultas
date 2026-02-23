# epr.CTProfileParams

**Schema:** epr
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Deprecated | bit |  |  | SI | - |
| PPDesc | varchar |  |  | NO | - |
| PPParameters | varchar |  |  | SI | ObsGroup | eAll | currPreg | revDate | DisplayComm... |
| PPShortDescription | varchar |  |  | SI | - |
| PPTypeDR | varchar |  | FK | NO | - |
| PP_Owner | varchar |  |  | SI | Owner |
| ReasonDeprecated | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*