# Region_CLXX_Integration_Nexus_CS.Email

**Schema:** Region_CLXX_Integration_Nexus_CS
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Nexus**. Conexión con sistema externo Nexus.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CharSet | varchar |  |  | SI | - |
| CreateDateTime | timestamp |  |  | NO | - |
| FileStream | longvarchar |  |  | SI | - |
| From | varchar |  |  | SI | - |
| MsgText | varchar |  |  | SI | - |
| Recepients | varchar |  |  | SI | - |
| Subject | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*